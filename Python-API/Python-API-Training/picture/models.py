from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Picture(models.Model):
    src = models.ImageField(upload_to="uploads/pictures/%Y/%m/%d/")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='picture_owner', on_delete=models.CASCADE)

    def __str__(self):
        return self.src.name
    
    class Meta:
        ordering = ['-created']