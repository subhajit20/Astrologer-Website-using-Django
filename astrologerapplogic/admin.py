from django.contrib import admin
from .models import WebsiteUser,Question,SocialLinks,Blog
# Register your models here.

admin.site.register(WebsiteUser)
admin.site.register(Question)
admin.site.register(SocialLinks)
admin.site.register(Blog)