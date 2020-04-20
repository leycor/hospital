#REST FRAMEWORK
from rest_framework import serializers

#MODEL
from hospital.core.models import Speciality
from hospital.users.api.serializers import DoctorHospitalSerializer


class SpecialitySerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=200, allow_blank=False, required=True)
    doctor = DoctorHospitalSerializer(read_only=True, many=True)

    class Meta:
        model = Speciality
        fields = ['id','name','doctor']