from rest_framework import viewsets
from .models import Doctor, Sick
from .serializers import UsersSerializer, SickSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = UsersSerializer

class SickViewSet(viewsets.ModelViewSet):
    queryset = Sick.objects.all()
    serializer_class = SickSerializer
