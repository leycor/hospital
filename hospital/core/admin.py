#DJANGO
from django.contrib import admin

#MODEL
from hospital.core.models import Speciality

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
