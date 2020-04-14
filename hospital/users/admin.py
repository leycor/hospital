#DJANGO
from django.contrib import admin
from django.contrib.auth import admin as auth_admin

#MODELS
from hospital.users.models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    readonly_fields = ('created','updated')
    list_display = ['username','is_doctor','is_admin','is_staff','name']
    list_filter = ['is_staff','is_admin','is_doctor']
