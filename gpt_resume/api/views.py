from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .serializers import JobSerializer, ApplicantSerializer, ApplicantSummarySerializer
from .models import Job, Applicant, Document
from .utils.resume_dispatcher import manage_pdf_files
from django.core.files.storage import FileSystemStorage
import uuid


class JobListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = JobSerializer

    queryset = Job.objects.all()


class JobCreateAPI(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = JobSerializer


class ApplicantListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = ApplicantSerializer

    def get_queryset(self):
        job_u_id = self.kwargs.get('job_u_id', None)
        if not job_u_id:
            raise Exception("Job id not found")
        jobs = Job.objects.filter(u_id=job_u_id)
        if not jobs.exists():
            raise Exception("Job not found")
        # Non-relevant applicants [Having relevance score less than 70]
        if "norec" in self.request.query_params:
            return Applicant.objects.filter(job_applied=jobs.first(), relevance__lt=70).order_by('-relevance')
        # Relevant applicants [Having relevance score greater than (or equal to) 70]
        elif "rec" in self.request.query_params:
            return Applicant.objects.filter(job_applied=jobs.first(), relevance__gte=70).order_by('-relevance')
        return Applicant.objects.filter(job_applied=jobs.first()).order_by('-relevance')

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ApplicantSummaryAPI(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = ApplicantSummarySerializer

    def get_object(self):
        u_id = self.kwargs.get('u_id', None)
        if not u_id:
            raise Exception("Applicant's Unique Id not found")
        applicants = Applicant.objects.filter(u_id=u_id)
        if not applicants.exists():
            raise Exception("Applicant not found")
        return applicants.first()

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ResumeUploadAPI(views.APIView):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        job_u_id = request.data.get('job_u_id', None)
        if not job_u_id:
            return Response({"message": "Job id not found"}, status=status.HTTP_400_BAD_REQUEST)
        jobs = Job.objects.filter(u_id=job_u_id)
        if not jobs.exists():
            return Response({"message": "Job not found"}, status=status.HTTP_400_BAD_REQUEST)
        files = request.FILES.getlist('files')
        responses = manage_pdf_files(files, job=jobs.first())
        return Response({"message": "Resumes uploaded successfully", "data": responses}, status=status.HTTP_201_CREATED)


class ResumeUploadWithJobAPI(views.APIView):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        job_title = request.POST.get("job_title")
        job_description = request.POST.get("job_description")
        documents = request.FILES.getlist("files")

        fs = FileSystemStorage()

        documents_list = []
        file_paths = []
        for document in documents:
            # Generate a random string for the filename
            filename = f"{uuid.uuid4()}.pdf"
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
        return Response({"message": "Resumes uploaded successfully", "data": responses, "job_u_id": job.u_id}, status=status.HTTP_201_CREATED)
