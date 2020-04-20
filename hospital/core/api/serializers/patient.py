#REST FRAMEWORK
from rest_framework import serializers

#MODELS
from hospital.core.models import Patient

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ['id','dni','first_name','last_name','date_birth']