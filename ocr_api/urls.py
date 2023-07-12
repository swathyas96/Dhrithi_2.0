from django.urls import path

from ocr_api.views import UploadOCRView


app_name = "ocr_api"

urlpatterns = [
    path("document/upload", UploadOCRView.as_view(), name="upload"),
]