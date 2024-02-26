from django.urls import path
from .views import *

urlpatterns = [

    # Applicant API endpoints
    # -----------------------

    # Get list of applicants for a unique job id [Used in Frontend]
    path('get-applicant-list/<uuid:job_u_id>/', ApplicantListAPI.as_view()),
    # Get summary of an applicant - the profile, projects, professional experience, etc. [Used in Frontend]
    path('get-applicant-summary/<uuid:u_id>/', ApplicantSummaryAPI.as_view()),
    # Post multiple pdf files with already existing `job_u_id`
    path('post-resume/', ResumeUploadAPI.as_view()),

    # Job API Endpoints
    # -----------------

    # Get list of unique job objects existing in the database
    path('get-job-list/', JobListAPI.as_view()),
    # Create a new job object with title and description
    path('post-job/', JobCreateAPI.as_view()),

    # Combined API Endpoint(s)
    # ------------------------

    # Post multiple pdf files with and `job_title` and `job_description`
    # It internally first creates a new job object and then creates new applicant objects
    path('post-resume-with-job/', ResumeUploadWithJobAPI.as_view()),
]
