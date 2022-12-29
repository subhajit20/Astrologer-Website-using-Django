from django.contrib import admin
from .models import WebsiteUser,SocialLinks,Blog,Question
# Register your models here.

admin.site.register(WebsiteUser)
admin.site.register(Question)
admin.site.register(SocialLinks)
admin.site.register(Blog)