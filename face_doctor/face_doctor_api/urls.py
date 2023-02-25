from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'doctors', views.DoctorViewSet)
router.register(r'sicks', views.SickViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
