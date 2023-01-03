from django.urls import path
from .views import GetLoginPage,Login,AdminHome,Social_Links,QuestionsPage
    
urlpatterns = [
    path('', GetLoginPage),
    path('login/',Login),
    path("adminhome/",AdminHome),
    path("Social-Links/",Social_Links),
    path("Question-page/",QuestionsPage)
] 