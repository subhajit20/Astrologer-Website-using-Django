from django.urls import path
from .views import GetLoginPage,Login,AdminHome,Social_Links,QuestionsPage,Admin_Blog,Admin_User
    
urlpatterns = [
    path('', GetLoginPage),
    path('login/',Login),
    path("adminhome/",AdminHome),
    path("Social-Links/",Social_Links),
    path("Question-page/",QuestionsPage),
    path("Admin-Blog/",Admin_Blog),
    path("Admin-user/",Admin_User),
] 