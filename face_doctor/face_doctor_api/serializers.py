from rest_framework import serializers
from .models import Sick, User, Drugs, Pharmacy


class SickSerializer(serializers.ModelSerializer):
    doctor_name = serializers.ReadOnlyField(source='doctor.doctor_name')

    class Meta:
        model = Sick
        fields =  '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = ['id', 'drug', 'barcode']


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ['id', 'pharmacyname', 'site', 'city', 'phone', 'email']
