from rest_framework import serializers
from .models import FileAll


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAll
        fields = '__all__'

