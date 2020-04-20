#REST FRAMEWORK
from rest_framework import serializers

#MODELS
from hospital.core.models import MedicalCheck

#SERIALIZERS
from hospital.core.api.serializers import PatientSerializer

class MedicalCheckSerializer(serializers.ModelSerializer):
    
    patient = PatientSerializer(read_only=True)

    class Meta:
        model = MedicalCheck
        fields = ['id','date','patient']