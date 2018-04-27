
from rest_framework import serializers

class ContentSerializer(serializers.Serializer):
    class Meta:
        fields = ('name')