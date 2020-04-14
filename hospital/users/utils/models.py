#DJANGO
from django.db import models

#REST FRAMEWORK
from rest_framework.validators import UniqueValidator

#UTILS
from hospital.utils.models import HospitalModel

#MODELS
from hospital.users.models import User


class UserModel(HospitalModel):
    
    #Personal Info
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    date_birth = models.DateField()

    #User data
    dni = models.PositiveIntegerField(blank=False,null=False, unique=True)
    password = models.CharField(max_length=200, blank=False, null=False)

    class Meta(HospitalModel.Meta):
        abstract = True
