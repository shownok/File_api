from django.db import models
from django.core.validators import FileExtensionValidator


class FileAll(models.Model):
    file = models.FileField(upload_to='files/', validators=[FileExtensionValidator(['pdf', 'pptx'])])
    added_date = models.DateTimeField()
