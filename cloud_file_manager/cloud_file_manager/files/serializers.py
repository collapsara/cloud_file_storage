from rest_framework import serializers

from . import models


class FileSerializer(serializers.ModelSerializer):
    filename = serializers.CharField(required=False, allow_null=True)
    content_type = serializers.CharField(required=False, allow_null=True)

    class Meta:
        model = models.File
        fields = "__all__"