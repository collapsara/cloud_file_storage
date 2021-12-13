from os import listdir

from django.http import FileResponse, HttpResponse
from rest_framework import views, viewsets, generics, status, parsers
from rest_framework.response import Response

from . import models
from . import serializers


class FileAPIView(generics.ListCreateAPIView):
 
    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def post(self, request, *args, **kwargs):
        request.data['content_type'] = request.FILES['file'].content_type
        request.data['filename'] = request.FILES['file'].name
        return super().post(request, *args, **kwargs)


class FileDownloadAPIview(generics.GenericAPIView):

    queryset = models.File.objects.all()
    serializer_class = serializers.FileSerializer

    def get(self, request, pk, *args, **kwargs):
        instance = self.get_object()
        response = HttpResponse(instance.file, content_type=instance.content_type)
        response['Content-Disposition'] = f'attachment; filename={instance.filename}'
        return response