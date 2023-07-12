from django.contrib import admin
from . import models


# @admin.site.register(models.OCR)
@admin.register(models.UploadOCRModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("filename", "uploaded_on", "uploaded_by") 

