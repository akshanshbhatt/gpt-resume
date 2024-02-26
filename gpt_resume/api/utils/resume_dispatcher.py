# This file contains the code for handling the resume files and extracting the relevant information from them.

# Python Libraries imports
from .base_prompt import base_function_prompt
from api.serializers import ApplicantSerializer
from api.models import Applicant, College, Project, ProfessionalExperience, Job
import os
import json

# Import for running multiple threads
from concurrent.futures import ThreadPoolExecutor, as_completed


# External Libraries imports
import fitz
from openai import OpenAI
from dotenv import load_dotenv

# Load the environment variables (OpenAI API Key)
load_dotenv()


# Internal code imports


class ApplicantHandler:

    def __init__(self, applicant: Applicant):
        self.applicant = applicant
        self.openai = OpenAI(api_key=os.getenv("OAI_API_KEY"))
        self.text = self._extract_text_data_from_pdf()

    def _update_resume(self, data: dict, relevance: int) -> None:
        self.applicant.resume_text = self.text
        self.applicant.name = data.get("name")
        self.applicant.email = data.get("email")
        self.applicant.relevance = relevance
        self.applicant.save()

    def _create_college(self, data: dict) -> None:
        College.objects.create(**data, applicant=self.applicant)

    def _create_project(self, data: dict) -> None:
        Project.objects.create(**data, applicant=self.applicant)

    def _create_professional_experience(self, data: dict) -> None:
        ProfessionalExperience.objects.create(**data, applicant=self.applicant)

    def _extract_text_data_from_pdf(self) -> str:
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
        # with open('_temporary.txt', 'w', encoding="utf-8") as file:
        #     file.write(text)

        return text

    def parse_resume(self):
        response = self.openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.text},
                {
                    "role": "user",
                    "content": f"Job Title: {self.applicant.job_applied.job_title} \nJob Description: {self.applicant.job_applied.job_description}",
                },
            ],
            functions=base_function_prompt,
            function_call="auto",
            temperature=1,
            # max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        # To store the json response in a file for debugging
        # with open('_temporary.json', 'w') as file:
        #     file.write(response.choices[0].message.function_call.arguments)
        return json.loads(response.choices[0].message.function_call.arguments)

    def populate_fields(self):
        # self.applicant.resume_text = "This is a test"
        # self.applicant.name = "John Doe"
        # self.applicant.email = "john@doe.com"
        # self.applicant.relevance = 2
        # self.applicant.save()
        final_data = self.parse_resume()
        self._update_resume(final_data.get("profile"),
                            final_data.get("relevance"))
        self._create_college(final_data.get("college"))
        for project in final_data.get("projects"):
            self._create_project(project)
        for professional_experience in final_data.get("professional_experiences"):
            self._create_professional_experience(professional_experience)


def handle_applicant(path: str, job: Job):
    serializer = ApplicantSerializer(
        data={"resume": path, "job_applied": job.u_id})
    if not serializer.is_valid():
        return serializer.errors

    print("Serializer is valid")
    applicant = serializer.save()
    print(applicant)
    try:
        applicant_handler = ApplicantHandler(applicant)
        applicant_handler.populate_fields()
        print("--\nSerialized and added successfully.\n--")
        return {"message": "Resume added successfully", "resume": serializer.data}
    except Exception as e:
        print(f"An error occurred while processing file {path}: {e}")
        applicant.delete()
        return {"message": str(e), "resume": serializer.data}


def manage_pdf_files(files: list, job: Job):
    responses = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(
            handle_applicant, file, job): file for file in files}

        for future in as_completed(futures):
            file = futures[future]
            try:
                responses.append(future.result())
            except Exception as e:
                print(f"An error occurred while processing file {file}: {e}")

    return responses
