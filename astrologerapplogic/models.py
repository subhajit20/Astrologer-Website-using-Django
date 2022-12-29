from django.db import models

# Create your models here.
class WebsiteUser(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50,editable=True)
    gender = models.CharField(max_length=50,editable=True)
    date = models.CharField(max_length=50,editable=True)
    month = models.CharField(max_length=50,editable=True)
    year = models.CharField(max_length=50,editable=True)
    email = models.EmailField() 
    hour = models.CharField(max_length=50,editable=True)
    minute = models.CharField(max_length=50,editable=True)
    country = models.CharField(max_length=50,editable=True)
    state = models.CharField(max_length=50,editable=True)


    @classmethod
    def CreateUser(cls,**kargs):
        newuser = cls.objects.create(**kargs)
        newuser.save()

        return True

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    question = models.CharField(max_length=200,editable=True)

    @classmethod
    def UploadQuestion(cls,**kargs):
        newuser = cls.objects.create(**kargs)
        newuser.save()

        return True


class SocialLinks(models.Model):
    socialId = models.AutoField(primary_key=True)
    socialmedianame = models.CharField(max_length=200,editable=True)
    link = models.URLField()

class Blog(models.Model):
    blogId = models.AutoField(primary_key=True)
    blogname = models.CharField(max_length=200,editable=True)
    blogimg = models.FileField(upload_to='static/')
    blogdesc = models.CharField(max_length=300)