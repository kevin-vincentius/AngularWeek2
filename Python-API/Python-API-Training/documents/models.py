from django.contrib.auth.models import User
from django.db import models


class Doc(models.Model):
    file = models.FileField(upload_to="uploads/files/%Y/%m/%d/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='doc_owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name

