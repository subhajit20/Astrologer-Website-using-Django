from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from . serializer import UserSerializer
from django.contrib.auth.hashers import (
    check_password
)
from .lib.token import get_tokens_for_user


def GetLoginPage(request):
    return render(request,"admin/Adminpage.html")



@api_view(['POST'])
def Login(request): 
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            checkuser = User.objects.filter(username=serializer.data["username"]).values_list("id","username","password")
            print(checkuser[0][0])
            if len(checkuser) > 0:
                isValidpassword = check_password(serializer.data["password"],checkuser[0][2]) 
                if isValidpassword:
                    iam = User.objects.get(username=serializer.data["username"])
                    datas = get_tokens_for_user(iam)
                    print(datas)
                    return Response({
                        "status":True,
                        "msg":"You have successfully logged in...",
                        "tokens":datas
                    })
                else:
                    return Response({
                        "status":False,
                        "msg":"Invalid username and password..."
                    })
            else:
                return Response({
                        "status":False,
                        "msg":"Invalid username and password..."
                    })  
        else:
            return Response({
                "status":False,
                "msg":serializer.errors
            })


def AdminHome(request):
    return render(request,"admin/AdminHome.html")