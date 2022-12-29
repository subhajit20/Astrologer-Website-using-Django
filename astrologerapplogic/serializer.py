from rest_framework import serializers
from .models import WebsiteUser,Question

class WebsiteUserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteUser
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"