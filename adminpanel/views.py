from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth.models import User

def Getadminpanel(request):
    return render(request,"admin/Adminpage.html")

@api_view(["POST"])
def Login(request):
    users = User.objects.all().values()
    return Response({
        "users":users
    })