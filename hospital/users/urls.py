#FROM DJANGO
from django.urls import path, include

#REST FRAMEWORK
from rest_framework import routers

#VIEWS
from hospital.users.api import views

#ROUTER
router = routers.DefaultRouter()
router.register(r'hospitals',views.HospitalUserViewSet, basename='hospitals')


#PATH
usertype_patterns = ([
    path('',include(router.urls)),
],'usertype')
