from django.urls import path
from . import views

urlpatterns = [
    path('test/',views.test, name='test'),
    path('report/',views.getReport, name='getReport'),
    path('getplace/',views.getPlace, name='getPlace'),
]