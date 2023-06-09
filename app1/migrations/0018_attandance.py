# Generated by Django 4.2 on 2023-04-29 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0017_delete_attandance"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attandance",
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
                ("name", models.CharField(max_length=40)),
                ("Date", models.CharField(max_length=20)),
                ("time", models.CharField(max_length=20)),
                ("Date_Time", models.CharField(max_length=20)),
                (
                    "company_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.company"
                    ),
                ),
                (
                    "device_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.device"
                    ),
                ),
                (
                    "employee_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.employee"
                    ),
                ),
            ],
        ),
    ]
