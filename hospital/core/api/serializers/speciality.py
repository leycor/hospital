#REST FRAMEWORK
from rest_framework import serializers

#MODEL
from hospital.core.models import Speciality
from hospital.users.api.serializers import DoctorHospitalSerializer


class SpecialitySerializer(serializers.ModelSerializer):

    doctor = DoctorHospitalSerializer(read_only=True, many=True)

    class Meta:
        model = Speciality
        fields = ['id','name','doctor']