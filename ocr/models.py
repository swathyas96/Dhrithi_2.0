import datetime
from django.db import models 
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


def upload_to(instance: dict[any, any], filename: str) -> str:
    return "documents/{uploaded_by}/{filename}".format(
        uploaded_by = instance.uploaded_by, filename=filename 
    ) 

class UploadOCRModel(models.Model):
    filename = models.CharField(max_length=250)
    file = models.FileField(_("File"), upload_to=upload_to)
    file_type = models.TextField(blank=True)
    number_of_pages = models.IntegerField(null=True)
    predicted_text = models.TextField(blank=True)
    uploaded_on = models.DateTimeField(default=datetime.datetime.now)
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self) -> str:
        return self.filename