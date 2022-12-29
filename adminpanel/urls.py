from django.urls import path
from .views import GetLoginPage,Login,AdminHome
    
urlpatterns = [
    path('', GetLoginPage),
    path('login/',Login),
    path("adminhome/",AdminHome)
] 