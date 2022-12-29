from django.urls import path
from .views import Getadminpanel,Login

urlpatterns = [
    path('', Getadminpanel),
    path('login/',Login)
] 