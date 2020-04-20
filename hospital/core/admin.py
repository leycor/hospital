#DJANGO
from django.contrib import admin

#MODEL
from hospital.core.models import Speciality, Patient, MedicalCheck

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

@admin.register(MedicalCheck)
class MedicalCheckAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
