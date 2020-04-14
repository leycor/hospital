#DJANGO
from django.db import models

#UTILS
from hospital.users.utils.models import UserModel

#MODELS
from hospital.users.models import User


class Doctor(UserModel):

    #Personal Info

    hospital = models.ForeignKey(User, related_name='hospital', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    