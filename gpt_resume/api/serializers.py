from rest_framework import serializers
from .models import Job, Applicant, College, Project, ProfessionalExperience


class JobSerializer(serializers.ModelSerializer):

    u_id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Job
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):

    u_id = None

    class Meta:
        model = College
        exclude = ['applicant', 'u_id']


class ProjectSerializer(serializers.ModelSerializer):

    u_id = None
    project_title = serializers.CharField(source='title')
    short_description = serializers.CharField(source='description')
    relevancy = serializers.IntegerField(source='relevance')

    class Meta:
        model = Project
        exclude = ['applicant', 'u_id', 'title', 'description', 'relevance']


class ProfessionalExperienceSerializer(serializers.ModelSerializer):

    u_id = None
    short_description = serializers.CharField(source='description')

    class Meta:
        model = ProfessionalExperience
        exclude = ['applicant', 'u_id', 'description']


class ApplicantSerializer(serializers.ModelSerializer):

    u_id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Applicant
        exclude = ['resume_text']
        extra_kwargs = {
            "name": {"read_only": True},
            "email": {"read_only": True},
            "relevance": {"read_only": True},
            "job_applied": {"write_only": True},
        }


class ApplicantSummarySerializer(serializers.ModelSerializer):

    u_id = serializers.UUIDField(read_only=True)
    college = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()
    professional_experiences = serializers.SerializerMethodField()

    class Meta:
        model = Applicant
        exclude = ['job_applied', 'resume_text']

    def get_college(self, obj):
        return CollegeSerializer(obj.college).data

    def get_projects(self, obj):
        return ProjectSerializer(obj.projects.order_by("-relevance"), many=True).data

    def get_professional_experiences(self, obj):
        return ProfessionalExperienceSerializer(obj.professional_experiences.order_by("-relevance"), many=True).data
