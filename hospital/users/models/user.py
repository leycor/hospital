#DJANGO
from django.db import models
from django.contrib.auth.models import AbstractUser

#UTILS
from hospital.utils.models import HospitalModel


class User(HospitalModel, AbstractUser):

    name = models.CharField('hospital name',max_length=200, blank=False, null=False)
    direction = models.CharField(max_length=200, blank=False, null=False)
    phone = models.CharField(max_length=15)
    is_doctor = models.BooleanField('doctor status',default=False)
    is_admin = models.BooleanField('admin status',default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','direction','phone','password']

    def __str__(self):
        return self.name
    