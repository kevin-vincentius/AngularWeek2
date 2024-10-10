from rest_framework import serializers

from documents.models import Doc


class DocSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField('meta_user')
    filename = serializers.SerializerMethodField("meta_file")

    def meta_user(self, instance):

        return {
            "username": instance.owner.username,
            "email": instance.owner.email
        }

    def meta_file(self, instance):
        return instance.file.name.split("/")[-1]
    class Meta:
        model = Doc
        fields = '__all__'
        read_only_fields = ['owner']



