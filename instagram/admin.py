from django.contrib import admin
from instagram.models import Image, Profile,Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Image)
admin.site.register(Comment)