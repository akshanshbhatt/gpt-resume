# from django.urls import path, include
# from rest_framework import routers
# from .views import ApplicantViewSet, ProjectViewSet, \
#     ProfessionalExperienceViewSet, CollegeViewSet, PDFFileViewSet


# router = routers.DefaultRouter()
# router.register(r'applicants', ApplicantViewSet)
# router.register(r'projects', ProjectViewSet)
# router.register(r'professional-experiences', ProfessionalExperienceViewSet)
# router.register(r'colleges', CollegeViewSet)
# router.register(r'pdf-files', PDFFileViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path
from .views import *

urlpatterns = [
    
    # Resume API
    path('get-applicant-list/<uuid:job_u_id>/', ApplicantListAPI.as_view()),
    path('get-applicant-summary/<uuid:u_id>/', ApplicantSummaryAPI.as_view()),
    path('post-resume/', ResumeUploadAPI.as_view()),
    
    # Job API
    path('job-list/', JobListAPI.as_view()),
    path('job-post/', JobCreateAPI.as_view()),
]
