#DJANGO
from django.db import models

#UTILS
from hospital.utils.models import HospitalModel

class UserModel(HospitalModel):

    dni = models.CharField(max_length=8, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    date_birth = models.DateField()

    class Meta(HospitalModel.Meta):
        abstract = True
    