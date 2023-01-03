from django.urls import path
from .views import CreateUsers,PostQuestion,Getalllinks,GetallBlogs,CreateLinks,Getallquestions,DeleteAquestions


urlpatterns = [
    path("c1/",CreateUsers),
    path('p1/',PostQuestion),
    path("l1/",Getalllinks),
    path("b1/",GetallBlogs),
    path("sl/",CreateLinks),
    path("q1/",Getallquestions),
    path("q2/",DeleteAquestions)
]
