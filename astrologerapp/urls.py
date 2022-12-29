from django.urls import path
from .views import Home,Kundali,KundaliMatching,Askyourastrologer,Blogpage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',Home),
    path('kundali/',Kundali),
    path('kundli-matching/',KundaliMatching),
    path('ask-yourastroger/',Askyourastrologer),
    path('blogs/',Blogpage),
]
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)