from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import WebsiteUserSerailizer,QuestionSerializer
from django.views.decorators.csrf import csrf_protect
from .models import WebsiteUser,Question,SocialLinks,Blog
from .task import Sending_Emails

# Create your views here.
@csrf_protect
@api_view(["POST"])
def CreateUsers(request):
    serializer = WebsiteUserSerailizer(data=request.data)
    if serializer.is_valid():
        print("Okk")
        print(serializer.data)
        WebsiteUser.CreateUser(**serializer.data)

        Sending_Emails(serializer.data['email'])
        return Response({
            "msg":{
                "flag":True,
                "success":"Okkk"
            }
        })
    else:
        print("Not Okk")
        return Response({
            "msg":{
                "flag":False,
                "error":serializer.errors
            }
        })



@csrf_protect
@api_view(["POST"])
def PostQuestion(request):
    serializer = QuestionSerializer(data=request.data)
    try:
        if serializer.is_valid():
            Question.UploadQuestion(**serializer.data)
            flag = Sending_Emails(serializer.data['email'])
            print(flag)
            if flag:
                return Response({
                    "msg":{
                        "flag":True,
                        "success":"Okkk"
                    }
                })
            else:
                return Response({
                    "msg":{
                        "flag":True,
                        "success":"Email has not been sent"
                    }
                })
        else:
            print(serializer.errors)
            return Response({
                "msg":{
                    "flag":False,
                    "error":serializer.errors
                }
            })
    except Exception as e:
        print(e)
        return Response({
            "msg":{
                "flag":False,
                "error":e
            }
        })


@api_view(["GET"])
def GetallBlogs(request):
    try:
        blogs = Blog.objects.all().values()
        if len(blogs) > 0:
            return Response({
                "msg":{
                    "status":True,
                    "blogs":blogs
                }
            })
        else:
            return Response({
                "msg":{
                    "flag":False,
                    "error":"No Blogs are there..."
                }
            })
    except Exception as e:
        return Response({
            "msg":{
                "flag":False,
                "error":"No blogs are there..."
            }
        })


@api_view(["GET"])
def Getalllinks(request):
    try:
        links = SocialLinks.objects.all().values()
        if len(links) > 0:
            return Response({
                "msg":{
                    "status":True,
                    "links":links
                }
            })
        else:
            return Response({
                "msg":{
                    "flag":False,
                    "error":"No links are there..."
                }
            })
    except Exception as e:
        return Response({
            "msg":{
                "flag":False,
                "error":"No links are there..."
            }
        })