#DJANGO
from django.db import models

#UTILS
from hospital.utils.models import HospitalModel

class Speciality(HospitalModel):
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)
    doctor = models.ManyToManyField('users.Doctor', related_name='specialties')

    def __str__(self):
        return self.name
    