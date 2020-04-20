#REST FRAMEWORK
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action

#MODELS
from hospital.core.models import Patient

#SERIALIZERS
from hospital.core.api.serializers import PatientSerializer

class PatientViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer