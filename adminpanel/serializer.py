from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
        