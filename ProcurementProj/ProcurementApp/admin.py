from django.contrib import admin
from .models import UserProfile, ContactMessage

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(ContactMessage)