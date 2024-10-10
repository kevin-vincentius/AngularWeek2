from django.forms import ValidationError

from rest_framework import viewsets, status
from rest_framework.response import Response
from picture.models import Picture
from picture.serializers import PictureSerializer

# Create your views here.
class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)