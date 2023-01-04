from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import WebsiteUserSerailizer,QuestionSerializer,SocialLinkSerializer,DeleteQuestionSerializer,DeleteLinkSerializer
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

@api_view(["POST"])
def CreateLinks(request):
    try:
        serializer = SocialLinkSerializer(data=request.data)
        if serializer.is_valid():
            newlink = SocialLinks.objects.create(socialmedianame=serializer.data["socialmedianame"],link=serializer.data["link"])
            newlink.save()

            return Response({
                "msg":{
                    "status":True,
                    "links":"Link has been created succefully..."
                }
            })
        else:
            return Response({
                "msg":{
                    "flag":False,
                    "error":serializer.errors
                }
            })
    except Exception as e:
        return Response({
            "msg":{
                "flag":False,
                "error":"Invalid name and link..."
            }
        })


# Get all questions views
@api_view(["GET"])
def Getallquestions(request):
    try:
        question = Question.objects.all().values()
        if len(question) > 0:
            return Response({
                "msg":{
                    "status":True,
                    "links":question
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

# Delete a questions - views
@api_view(["POST"])
def DeleteAquestions(request):
    try:
        serializer = DeleteQuestionSerializer(data=request.data)
        if serializer.is_valid():
            Question.objects.filter(id=serializer.data["id"]).delete()
            return Response({
                "msg":{
                    "status":True,
                    "links":"Question is Deleted"
                }
            })
        else:
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
                "error":"Soemthing went wrong..."
            }
        })

# Delete a questions - views
@api_view(["POST"])
def DeleteAlink(request):
    try:
        serializer = DeleteLinkSerializer(data=request.data)
        if serializer.is_valid():
            SocialLinks.objects.filter(socialId=serializer.data["id"]).delete()
            return Response({
                "msg":{
                    "status":True,
                    "links":"Link is is Deleted"
                }
            })
        else:
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
                "error":"Soemthing went wrong..."
            }
        })