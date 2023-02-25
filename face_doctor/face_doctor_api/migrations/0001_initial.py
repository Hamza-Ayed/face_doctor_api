# Generated by Django 4.1.7 on 2023-02-25 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("doctor_name", models.CharField(max_length=88)),
                ("password", models.CharField(max_length=66)),
                ("device_id", models.CharField(default="11221", max_length=100)),
                (
                    "roles_id",
                    models.SmallIntegerField(
                        choices=[(1, "doctor"), (2, "secretary"), (3, "admin")]
                    ),
                ),
                ("phone", models.CharField(max_length=20)),
                ("clinic_name", models.CharField(max_length=200)),
                ("date_register", models.DateField()),
                ("reg", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="Drugs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("drug_name", models.CharField(max_length=100, null=True)),
                ("barcode", models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name="Pharmacy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pharmacyname", models.CharField(max_length=200)),
                ("site", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("sick", "Sick"),
                            ("doctor", "Doctor"),
                            ("secretary", "Secretary"),
                            ("admin", "Admin"),
                        ],
                        max_length=20,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("first_name", models.CharField(blank=True, max_length=30)),
                ("last_name", models.CharField(blank=True, max_length=30)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Sick",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("birth_date", models.DateField()),
                ("telephone", models.CharField(max_length=15)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")], max_length=10
                    ),
                ),
                ("site", models.CharField(default="0", max_length=150)),
                ("date_register", models.DateField()),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="face_doctor_api.doctor",
                    ),
                ),
            ],
        ),
    ]