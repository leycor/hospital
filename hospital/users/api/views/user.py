#REST FRAMEWORK
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAdminUser

#MODELS
from hospital.users.models import User

#SERIALIZERS
from hospital.users.api.serializers import UserHospitalSerializer, CreateUserHospitalSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = User.objects.filter(is_staff=True)
    serializer_class = UserHospitalSerializer

    def create(self, request, *args, **kwargs):
        serializer = CreateUserHospitalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
