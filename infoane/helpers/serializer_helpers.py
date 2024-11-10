from rest_framework import serializers
from infoane.serializers.fields import CustomIntegerField, CustomCharField


class SuccessResponseSerializer(serializers.Serializer):
    status = CustomIntegerField(required=True)
    message = CustomCharField(required=True)