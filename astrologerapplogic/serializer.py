from rest_framework import serializers
from .models import WebsiteUser,Question,SocialLinks

class WebsiteUserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteUser
        fields = "__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
    
class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = "__all__"

class DeleteQuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class DeleteLinkSerializer(serializers.Serializer):
    id = serializers.IntegerField()