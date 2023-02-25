from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class Doctor(models.Model):
    ROLES = (
        (1, 'doctor'),
        (2, 'secretary'),
        (3, 'admin')
    )
    doctor_name = models.CharField(max_length=88)
    password = models.CharField(max_length=66)
    device_id = models.CharField(max_length=100, default='11221')
    roles_id = models.SmallIntegerField(choices=ROLES)
    phone = models.CharField(max_length=20)
    clinic_name = models.CharField(max_length=200)
    date_register = models.DateField()
    reg = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.doctor_name} ({self.clinic_name})'


class Pharmacy(models.Model):
    pharmacyname = models.CharField(max_length=200)
    site = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.pharmacyname


class Sick(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    telephone = models.CharField(max_length=15)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=(('male', 'Male'), ('female', 'Female')))
    site = models.CharField(max_length=150, default='0')
    date_register = models.DateField()

    def __str__(self):
        return self.name


class Drugs(models.Model):
    drug_name = models.CharField(max_length=100, null=True)
    barcode = models.CharField(max_length=150)

    def __str__(self):
        return self.drug_name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    USER_ROLES = (
        ('sick', 'Sick'),
        ('doctor', 'Doctor'),
        ('secretary', 'Secretary'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
