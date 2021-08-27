from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .serializers import GenericFileUpload, GenericFileUploadSerializer

# Create your views here.


class GenericFileUploadView(ModelViewSet):
    queryset = GenericFileUpload.objects.all()
    serializer_class = GenericFileUploadSerializer
