from django.db import models

#UTILS
from hospital.utils.models import HospitalModel

class MedicalCheck(HospitalModel):
    
    #Personal Info
    date = models.DateField()
    patient = models.ForeignKey('core.Patient', related_name='checks', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date)
    
    
