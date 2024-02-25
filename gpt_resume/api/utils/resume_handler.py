import sys, os
# sys.path.append('../')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gpt_resume.settings')

# Django Imports
# import django
# django.setup()
# from django.conf.global_settings import MEDIA_ROOT

import json

# Import for running multiple threads
import concurrent.futures


# External Libraries imports
import fitz
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


# Internal code imports
from api.models import Applicant, College, Project, ProfessionalExperience, Job
from api.serializers import ApplicantSerializer
from .handler_functions import JSON_FUNCTION


class ApplicantHandler:
    
    def __init__(self, applicant: Applicant):
        self.applicant = applicant
        self.openai = OpenAI(api_key=os.getenv("OAI_API_KEY"))
        self.text = self._extract_data_from_pdf()

    def _update_resume(self, data: dict, relevance: int):
        self.applicant.resume_text = self.text
        self.applicant.name = data.get('name')
        self.applicant.email = data.get('email')
        self.applicant.relevance = relevance
        self.applicant.save()
    
    def _create_college(self, data: dict):
        College.objects.create(**data, applicant=self.applicant)
    
    def _create_project(self, data: dict):
        Project.objects.create(**data, applicant=self.applicant)
    
    def _create_professional_experience(self, data: dict):
        ProfessionalExperience.objects.create(**data, applicant=self.applicant)

    def _extract_data_from_pdf(self) -> str:
        doc = fitz.open(self.applicant.resume[1:])
        text = ""
        # If the pdf is more than 3 pages, only extract the first 3 pages
        # This is done as a safety measure to prevent the server from crashing
        _pages = 0
        for page in doc:
            text += page.get_text()
            text += "\n"
            _pages += 1
            if _pages >= 3:
                break
        doc.close()

        # Use for debugging when there is any issue with the text extraction
        # with open('__temporary.txt', 'w', encoding="utf-8") as file:
        #     file.write(text)

        return text

    def parse_resume(self):
        response = self.openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.text},
                {"role": "user", "content": f"Role: {self.applicant.job_applied.job_title} \nDescription : {self.applicant.job_applied.job_description}"}
            ],
            functions=JSON_FUNCTION,
            function_call='auto'
        )
        print("RAN THIS FUNCTION")
        with open('random.json', 'w') as file:
            file.write(response.choices[0].message.function_call.arguments)
        return json.loads(response.choices[0].message.function_call.arguments)
        
    def populate_fields(self):
        # self.applicant.resume_text = "This is a test"
        # self.applicant.name = "John Doe"#data.get('name')
        # self.applicant.email = "john@doe.com"#data.get('email')
        # self.applicant.relevance = 2#relevance
        # self.applicant.save()
        final_data = self.parse_resume()
        self._update_resume(final_data.get('profile'), final_data.get('relevance'))
        self._create_college(final_data.get('college'))
        for project in final_data.get('projects'):
            self._create_project(project)
        for professional_experience in final_data.get('professional_experiences'):
            self._create_professional_experience(professional_experience)


def handle_applicant(path: str, job: Job):
    serializer = ApplicantSerializer(data={'resume': path, 'job_applied': job.u_id})
    if serializer.is_valid():
        print("Serializer is valid")
        applicant = serializer.save()
        print(applicant)
    else:
        return serializer.errors

    try:
        applicant_handler = ApplicantHandler(applicant)
        applicant_handler.populate_fields()
        print("--\nSerialized and added successfully.\n--")
        return {
            "message": "Resume added successfully",
            "resume": serializer.data
        }
    except Exception as e:
        print("ran this")
        applicant.delete()
        return {
            "message": str(e),
            "resume": serializer.data
        }

def manage_pdf_files(files: list, job: Job):
    responses = []
    with concurrent.futures.ThreadPoolExecutor(6) as executor:
        responses = executor.map(handle_applicant, files, [job]*len(files))
    return responses
    # for file in files:
    #     responses.append(handle_applicant(file, job))
    
    # applicant_list = [Applicant(resume=file, job_applied=job) for file in files]
    # Applicant.objects.bulk_create(applicant_list)

    return responses
