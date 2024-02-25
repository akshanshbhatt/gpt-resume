# from django.shortcuts import render

# from rest_framework import viewsets
# from api.models import Applicant, Project, ProfessionalExperience, College, PDFFile
# from api.serializers import ApplicantSerializer, ProjectSerializer, ProfessionalExperienceSerializer, CollegeSerializer, PDFFileSerializer


# class PDFFileViewSet(viewsets.ModelViewSet):
#     queryset = PDFFile.objects.all()
#     serializer_class = PDFFileSerializer

# class ApplicantViewSet(viewsets.ModelViewSet):
#     queryset = Applicant.objects.all()
#     serializer_class = ApplicantSerializer


# class ProjectViewSet(viewsets.ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# class ProfessionalExperienceViewSet(viewsets.ModelViewSet):
#     queryset = ProfessionalExperience.objects.all()
#     serializer_class = ProfessionalExperienceSerializer

# class CollegeViewSet(viewsets.ModelViewSet):
#     queryset = College.objects.all()
#     serializer_class = CollegeSerializer
from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


from .serializers import JobSerializer, ApplicantSerializer, ApplicantSummarySerializer
from .models import Job, Applicant
from .utils.resume_handler import manage_pdf_files


class JobListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = JobSerializer
    queryset = Job.objects.filter(hidden=False)

class JobCreateAPI(generics.CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = JobSerializer

class ApplicantListAPI(generics.ListAPIView):

    permission_classes = (AllowAny,)
    serializer_class = ApplicantSerializer

    def get_queryset(self):
        job_u_id = self.kwargs.get('job_u_id',None)
        if not job_u_id:
            raise Exception("Job static id not found")
        jobs = Job.objects.filter(u_id=job_u_id)
        if not jobs.exists():
            raise Exception("Job not found")
        return Applicant.objects.filter(job_applied=jobs.first()).order_by('-relevance')

    def list(self, request, *args, **kwargs):
        try:
            return super().list(request, *args, **kwargs)
        except Exception as e:
            return Response({"message":str(e)},status=status.HTTP_400_BAD_REQUEST)


class ApplicantSummaryAPI(generics.RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = ApplicantSummarySerializer

    def get_object(self):
        u_id = self.kwargs.get('u_id', None)
        if not u_id:
            raise Exception("Unique Id not found")
        applicants = Applicant.objects.filter(u_id=u_id)
        if not applicants.exists():
            raise Exception("Applicant not found")
        return applicants.first()

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Exception as e:
            return Response({"message": str(e)},status=status.HTTP_400_BAD_REQUEST)


class ResumeUploadAPI(views.APIView):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        job_u_id = request.data.get('job_u_id', None)
        if not job_u_id:
            return Response({"message":"Job id not found"}, status=status.HTTP_400_BAD_REQUEST)
        jobs = Job.objects.filter(u_id=job_u_id)
        if not jobs.exists():
            return Response({"message":"Job not found"}, status=status.HTTP_400_BAD_REQUEST)
        files = request.FILES.getlist('files')
        responses = manage_pdf_files(files, job=jobs.first())
        return Response({"message": "Resumes uploaded successfully", "data": responses}, status=status.HTTP_201_CREATED)
