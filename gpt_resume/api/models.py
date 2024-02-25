import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Job(models.Model):
    u_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_title = models.TextField(blank=False, verbose_name="Job Title")
    job_description = models.TextField(blank=False, verbose_name="Job Description")
    hidden = models.BooleanField(default=False)


class Applicant(models.Model):
    u_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(blank=True, verbose_name="Applicant's Name")
    email = models.EmailField(blank=True, verbose_name="Applicant's Email")
    resume = models.TextField(blank=False, verbose_name="Applicant's Resume Path")
    resume_text = models.TextField(blank=True, verbose_name="Applicant's Resume Text Content")
    job_applied = models.ForeignKey(Job, on_delete=models.CASCADE, verbose_name="Job Applied For")
    relevance = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)],
                                    verbose_name="Relevance Score")


class College(models.Model):
    u_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(blank=True, verbose_name="College Name")
    branch = models.TextField(blank=True, verbose_name="Branch of Study")
    degree = models.TextField(blank=True, verbose_name="Degree")
    start_date = models.CharField(max_length=7, blank=True, verbose_name="Start Date")
    end_date = models.CharField(max_length=7, blank=True, verbose_name="End Date")
    applicant = models.OneToOneField(Applicant, on_delete=models.CASCADE, related_name="college")


class Project(models.Model):
    u_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(blank=True, verbose_name="Project Title")
    description = models.TextField(blank=True, verbose_name="Project Description")
    tech_stack = models.JSONField(blank=True, verbose_name="Tech Stack Used")
    time_duration = models.JSONField(blank=True, verbose_name="Time Duration")
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="projects")
    relevance = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)],
                                    verbose_name="Relevance Score")


class ProfessionalExperience(models.Model):
    u_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.TextField(blank=True, verbose_name="Role")
    organization = models.TextField(blank=True, verbose_name="Organization Name")
    description = models.TextField(blank=True, verbose_name="Description")
    tech_stack = models.JSONField(blank=True, verbose_name="Tech Stack Used")
    time_duration = models.JSONField(blank=True, verbose_name="Time Duration")
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='professional_experiences')
    relevance = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)],
                                    verbose_name="Relevance Score")
