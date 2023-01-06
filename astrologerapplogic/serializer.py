from rest_framework import serializers
from .models import WebsiteUser,Question,SocialLinks,Blog

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

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields = "__all__"

    def validate_blogname(self, value):
        if value is None:
            raise serializers.ValidationError("Enter Blogname")
        else:
            return value
    def validate_blogdesc(self, value):
        if value is None:
            raise serializers.ValidationError("Enter Blog Description")
        else:
            return value

class DeleteBlogSerializer(serializers.Serializer):
    blogId = serializers.CharField()