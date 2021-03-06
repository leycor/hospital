#DJANGO
from django.db import models

#UTILS
from hospital.utils.models import HospitalModel

class Patient(HospitalModel):
    
    #Personal Info
    dni = models.PositiveIntegerField(blank=False,null=False, unique=True)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    date_birth = models.DateField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
