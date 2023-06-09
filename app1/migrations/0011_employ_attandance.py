# Generated by Django 4.2 on 2023-04-27 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0010_remove_employ_device_id_delete_attandance_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employ",
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
                ("employ_id", models.IntegerField()),
                ("employ_uid", models.IntegerField()),
                ("name", models.CharField(max_length=100)),
                ("Is_sent", models.IntegerField(default=0)),
                (
                    "device_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.device"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Attandance",
            fields=[
                ("attandance_id", models.AutoField(primary_key=True, serialize=False)),
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
                    "employ_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app1.employ"
                    ),
                ),
            ],
        ),
    ]
