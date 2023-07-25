from django.urls import path

from ocr_api.views import ExportToDOCX, OCRPDFView, UploadOCRView


app_name = "ocr_api"

urlpatterns = [
    path("document/upload", UploadOCRView.as_view(), name="upload"),
    path("document/extract_pdf", OCRPDFView.as_view(), name="extract"),
    path("document/exportDoc", ExportToDOCX.as_view(), name="exportDoc"),
]
