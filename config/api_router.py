from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from hospital.users.api import views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("hospitals", views.HospitalUserViewSet, basename="hospitals")


app_name = "api"
urlpatterns = router.urls
