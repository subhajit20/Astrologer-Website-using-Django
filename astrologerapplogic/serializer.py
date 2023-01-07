from rest_framework import serializers
from .models import WebsiteUser,Question,SocialLinks,Blog
from django.contrib.auth.models import User

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    def validate_username(self,value):
        users = User.objects.filter(username=value).values()
        if len(users) > 0:
            raise serializers.ValidationError("Username is already exist...")
        else:
            return value

    def validate_password(self,value):
        confirmpassword = self.context.get("confirmpassword")
        if value == confirmpassword:
            return value
        else:
            raise serializers.ValidationError("Password and confirmpassword is are not matched...")
    
class DeleteUserSerializer(serializers.Serializer):
    id = serializers.CharField()