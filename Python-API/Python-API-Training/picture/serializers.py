from rest_framework import serializers
from picture.models import Picture

class PictureSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    filename = serializers.SerializerMethodField()

    def get_user(self, instance):
        return {
            "username": instance.owner.username,
            "email": instance.owner.email
        }

    def get_filename(self, instance):
        return instance.src.name.split("/")[-1]

    class Meta:
        model = Picture
        fields = '__all__'
        read_only_fields = ['owner']
