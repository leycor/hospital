from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

#USER VIEWS
from hospital.users.api import views as views_users

#CORE VIEWS
from hospital.core.api import views as views_core



if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

#ROUTER USER
router.register("hospitals", views_users.HospitalUserViewSet, basename="hospitals")
router.register("doctors", views_users.DoctorUserViewSet, basename="doctors")

#ROUTER CORE
router.register('specialties',views_core.SpecialityViewSet, basename="specialties")
router.register('patients',views_core.PatientViewSet, basename="patients")
router.register('checks',views_core.MedicalCheckViewSet, basename="checks")


app_name = "api"
urlpatterns = router.urls
