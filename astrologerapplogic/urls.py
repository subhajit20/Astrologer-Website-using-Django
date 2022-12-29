from django.urls import path
from .views import CreateUsers,PostQuestion,Getalllinks,GetallBlogs

urlpatterns = [
    path("c1/",CreateUsers),
    path('p1/',PostQuestion),
    path("l1/",Getalllinks),
    path("b1/",GetallBlogs)
]
