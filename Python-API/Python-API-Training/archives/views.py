from django.shortcuts import render


from archives.models import Archive, FileArchive
from archives.serializers import ArchiveSerializer, FileArchiveSerializer
from rest_framework import permissions, viewsets


class ArchiveViewSet(viewsets.ModelViewSet):
    queryset = Archive.objects.all()
    serializer_class = ArchiveSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileArchiveViewSet(viewsets.ModelViewSet):
    queryset = FileArchive.objects.all()
    serializer_class = FileArchiveSerializer
