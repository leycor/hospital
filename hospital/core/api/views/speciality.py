#REST FRAMEWORK
from rest_framework import viewsets, mixins, status
from rest_framework.decorators import action

#MODELS
from hospital.core.models import Speciality

#SERIALIZERS
from hospital.core.api.serializers import SpecialitySerializer

class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer