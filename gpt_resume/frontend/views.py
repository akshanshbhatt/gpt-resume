from django.shortcuts import render
from .models import Document
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import uuid
from api.models import Job
from api.utils.resume_handler import manage_pdf_files

def index(request):
    if request.method == "POST":
        job_title = request.POST.get("job_title")
        job_description = request.POST.get("job_description")
        documents = request.FILES.getlist("documents")

        fs = FileSystemStorage()

        documents_list = []
        file_paths = []
        for document in documents:
            # Generate a random string for the filename
            filename = "{}.pdf".format(uuid.uuid4())
            filename = fs.save(filename, document)
            doc = Document(document=filename)
            documents_list.append(doc)
            file_paths.append(fs.url(filename))

        Document.objects.bulk_create(documents_list)

        job = Job(job_title=job_title, job_description=job_description)
        # print("FILE PATHS: ", file_paths)
        job.save()

        responses = manage_pdf_files(files=file_paths, job=job)
        print("-------\n", responses, "\n-------")

        messages.success(request, "Resumes Uploaded")

    return render(request, "index.html")

# from .utils import convert_pdfs_in_folder

# def index(request):
#     if request.method == "POST":
#         job_title = request.POST.get("job_title")
#         job_description = request.POST.get("job_description")
#         documents = request.FILES.getlist("documents")
#         documents_list = [Document(document=document) for document in documents]
#         Document.objects.bulk_create(documents_list)

#         job = Job(title=job_title, description=job_description)
#         job.save()

#         # convert_pdfs_in_folder("temp_files/resume", "temp_files/resume_text")

#         # print(f"{job_description}: {job_title}")

#         messages.success(request, "Resumes Uploaded")

#     return render(request, "index.html")
