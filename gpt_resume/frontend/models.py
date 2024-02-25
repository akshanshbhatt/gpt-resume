from django.db import models
from django.core.validators import FileExtensionValidator

class Document(models.Model):
    document = models.FileField(upload_to='resume/',
                              validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
                              verbose_name="Applicant's Resume")

    def __str__(self):
        return str(self.id)
