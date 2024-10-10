
from rest_framework import serializers

from .models import Archive, FileArchive


class ArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = '__all__'
        read_only_fields = ['user']


class FileArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileArchive
        fields = '__all__'