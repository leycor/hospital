#REST FRAMEWORK
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action

#MODELS
from hospital.core.models import MedicalCheck

#SERIALIZERS
from hospital.core.api.serializers import MedicalCheckSerializer

class MedicalCheckViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = MedicalCheck.objects.all()
    serializer_class = MedicalCheckSerializer