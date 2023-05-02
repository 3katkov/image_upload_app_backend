from django.contrib import admin
from .models import Plan, ImageModel, UserProfile

admin.site.register(Plan)
admin.site.register(UserProfile)
admin.site.register(ImageModel)