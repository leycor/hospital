#REST FRAMEWORK
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

#MODELS
from hospital.users.models import User



class UserHospitalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','name','direction','phone']

class CreateUserHospitalSerializer(serializers.ModelSerializer):
    

    #Hospital Data
    name = serializers.CharField(min_length=3, max_length=200, allow_blank=False, required=True)
    direction = serializers.CharField(min_length=3, max_length=200, allow_blank=False, required=True)
    phone = serializers.CharField(min_length=10, max_length=15)

    #User Data
    username = serializers.CharField(min_length=3, max_length=45, allow_blank=False, required=True,
                                    validators=[UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(min_length=8, max_length=64)
    
    class Meta:
        model = User
        fields = ['id','name','direction','phone','username','password']

    #Create new hospital
    def create(self, validated_data):
        return User.objects.create(**validated_data, is_staff=True) 