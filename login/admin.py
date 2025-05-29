from django.contrib import admin
from .models import CustomUser, ProfileUpdate

admin.site.register(CustomUser)
admin.site.register(ProfileUpdate)