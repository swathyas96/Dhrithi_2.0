from rest_framework import serializers

from ocr.models import UploadOCRModel


class UploadOCRSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "filename",
            "file",
            "file_type",
            "number_of_pages",
            "predicted_text",
            "uploaded_by",
            "uploaded_on",
        )
        model = UploadOCRModel    
