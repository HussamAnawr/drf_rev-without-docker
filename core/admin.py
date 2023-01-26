from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ['email', 'first_name', 'last_name']

admin.site.register(models.User, UserAdmin)