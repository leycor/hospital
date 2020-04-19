#REST FRAMEWORK
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#MODELS
from hospital.users.models import User, Doctor

#SERIALIZERS
from hospital.users.api.serializers import UserHospitalSerializer


class DoctorHospitalSerializer(serializers.ModelSerializer):

    hospital = UserHospitalSerializer(read_only=True)
    specialties = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Doctor
        fields = ['id','username','dni','first_name','last_name','date_birth','specialties','hospital']

class CreateDoctorHospitalSerializer(serializers.ModelSerializer):

    #Hospital Data
    dni = serializers.IntegerField(min_value=8,required=True)
    first_name = serializers.CharField(min_length=3, max_length=200, allow_blank=False, required=True)
    last_name = serializers.CharField(min_length=3, max_length=200, allow_blank=False, required=True)

    #User Data
    username = serializers.CharField(max_length=200, allow_blank=False, required=True,
                                    validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(min_length=8, max_length=64)
    
    class Meta:
        model = Doctor
        fields = ['id','dni','first_name','last_name','date_birth','username', 'password']
    
    def create(self, validated_data):
        hospital = self._kwargs['data']['hospital']
        return Doctor.objects.create(**validated_data,hospital=hospital) 
