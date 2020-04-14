from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAdminUser

#MODELS
from hospital.users.models import User, Doctor

#SERIALIZERS
from hospital.users.api.serializers import DoctorHospitalSerializer, CreateDoctorHospitalSerializer


class DoctorUserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):

    queryset = Doctor.objects.all()
    serializer_class = DoctorHospitalSerializer

    def create(self, request, *args, **kwargs):
        request.data['hospital'] = request.user
        serializer = CreateDoctorHospitalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
