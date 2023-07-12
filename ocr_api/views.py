import json

from ocr_api.utils import save_image_from_in_memory_image
from .serializers import (
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
            request.data["number_of_pages"] = 1
            image = save_image_from_in_memory_image(
                request.data["file"].read(),
                request.data["filename"],
                request.data["file"].content_type.split("/")[-1],
            )
            text = image_to_string(image, lang='eng+mal')
            request.data["predicted_text"] = str(text)
            serializer = UploadOCRSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
