from django.db import models
from django.contrib.auth.models import User


class Archive(models.Model):
    title = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='user_archive', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title


class FileArchive(models.Model):
    file = models.FileField()
    archive = models.OneToOneField(Archive, related_name='filearchive_archive', on_delete=models.CASCADE)

    def __str__(self):
        return self.archive.title