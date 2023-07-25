import json

from ocr_api.utils import (
    convert_pdf_to_docx,
    get_image_from_path,
    pdf_to_images,
    save_image_from_in_memory_image,
)
from .serializers import (
    ExportPDFSerializer,
    UploadOCRSerializer,
)
from ocr.models import UploadOCRModel
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


from pytesseract import image_to_string


class UploadOCRView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request: any, format: any = None):
        print(request.data)
        if request.data["file"] != None:

            if request.data["file"].content_type == "application/pdf":
                images = pdf_to_images(request.data["file"].read(), request.data["filename"])
                request.data["number_of_pages"] = len(images)
            else:
                request.data["number_of_pages"] = 1
                images = [
                    save_image_from_in_memory_image(
                        request.data["file"].read(),
                        request.data["filename"],
                        request.data["file"].content_type.split("/")[-1],
                    )
                ]
            text = image_to_string(images[0], lang="eng+mal")
            request.data["predicted_text"] = str(text)
            serializer = UploadOCRSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class OCRPDFView(APIView):
    permission_classes = [permissions.AllowAny]
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request: any, format: any = None):
        if request.data["upload_ocr_id"] != None:
            ocr = UploadOCRModel.objects.filter(id=request.data["upload_ocr_id"])
            if ocr != []:
                image = get_image_from_path(
                    f'documents/pdf2image/{ocr[0].filename}/{request.data["page_number"]}.png'
                )
                text = image_to_string(image, lang="eng+mal")
                return Response({"text": str(text)}, status=status.HTTP_200_OK)
        return Response({"message": "failed"}, status=status.HTTP_400_BAD_REQUEST)

class ExportToDOCX(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request: any, format: any = None) -> any:
        print(request.data)
        if request.data["file"] != None:
            if request.data["file"].content_type == "application/pdf":
                print(request.data["file"].read())
        serializer = ExportPDFSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data["file"])
            convert_pdf_to_docx(serializer.data["file"])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)