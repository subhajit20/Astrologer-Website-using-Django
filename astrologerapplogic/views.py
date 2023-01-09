from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,parser_classes,APIView
from .serializer import WebsiteUserSerailizer,QuestionSerializer,SocialLinkSerializer,DeleteQuestionSerializer,DeleteLinkSerializer,BlogSerializer,DeleteBlogSerializer,UserSerializer,DeleteUserSerializer
from django.views.decorators.csrf import csrf_protect
from .models import WebsiteUser,Question,SocialLinks,Blog
from .task import Sending_Emails
from rest_framework.parsers import MultiPartParser,FormParser

from django.contrib.auth.models import User
from django.contrib.auth.hashers import (
    make_password
)

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
    try:
        serializer = QuestionSerializer(data=request.data)
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
                        "flag":False,
                        "success":"Email has not been sent"
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


class UploadBlog(APIView):
        """
        A view that can accept POST requests with JSON content.
        """
        parser_classes = ( MultiPartParser, FormParser)

        def post(self, request, format=None):
            serializer = BlogSerializer(data=request.data)
            if serializer.is_valid():
                flag = Blog.Upload(request.FILES.get("blogimg"),**serializer.data)
                if flag:
                    return Response({
                        "status":True,
                        "msg":"File Uploaded Successfully..."
                    })
                else:
                    return Response({
                        "status":False,
                        "msg":"Failed..."
                    })
            else:
                return Response({
                    "status":False,
                    "msg":serializer.errors
                })


@api_view(["POST"])
def DeleteBlog(request):
    try:
        serializer = DeleteBlogSerializer(data=request.data)

        if serializer.is_valid():
            flag = Blog.Delete(serializer.data["blogId"])
            if flag:
                return Response({
                    "status":True,
                    "msg":"Blog is deleted Succesfully..."
                })
            else:
                return Response({
                    "status":True,
                    "msg":"Failed to Delete Blog..."
                })
        else:
            return Response({
                "status":True,
                "msg":serializer.errors
            })
    except Exception as e:
        print(e)
        return Response({
            "status":False,
            "msg":"Something Went Wrong..."
        })

@api_view(["POST"])
def CreateUser(request):
    try:
        serializer = UserSerializer(data=request.data,context=request.data)

        if serializer.is_valid():
            newpassword = make_password(serializer.data["password"])
            newuser = User.objects.create(username=serializer.data["username"],password=newpassword)
            newuser.save()
            return Response({
                "status":True,
                "msg":"New User has been created successfully..."
            })
        else:
            return Response({
                "status":True,
                "msg":serializer.errors
            })
    except Exception as e:
        print(e)
        return Response({
            "status":False,
            "msg":"Something Went Wrong..."
        })


@api_view(["GET"])
def Get_ALL_User(request):
    try:
        users = User.objects.all().values_list("id","username","password")

        if len(users) > 0:
            return Response({
                "status":True,
                "data":users
            })
        else:
            return Response({
                "status":False,
                "data":"No such users found..."
            })
    except Exception as e:
        print(e)
        return Response({
            "status":False,
            "msg":"Something Went Wrong..."
        })


@api_view(["POST"])
def DeleteAUser(request):
    try:
        serializer = DeleteUserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.filter(id=serializer.data["id"]).delete()

            return Response({
                "status":True,
                "msg":"User is delete succefully..."
            })
        else:
            return Response({
                    "status":False,
                    "data":serializer.errors
                })
    except Exception as e:
        print(e)
        return Response({
            "status":False,
            "msg":"Something Went Wrong..."
        })