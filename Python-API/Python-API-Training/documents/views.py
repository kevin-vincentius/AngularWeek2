from django.shortcuts import render
from rest_framework import viewsets

from documents.models import Doc
from documents.serializers import DocSerializer


#
# from documents.models import Document, Vendor, Storage
# from documents.serializers import DocumentSerializer, VendorSerializer, StorageSerializer
#
#
class DocViewSet(viewsets.ModelViewSet):
    queryset = Doc.objects.all()
    serializer_class = DocSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



#
#
# class VendorViewSet(viewsets.ModelViewSet):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer
#
#
# class StorageViewSet(viewsets.ModelViewSet):
#     queryset = Storage.objects.all()
#     serializer_class = StorageSerializer

