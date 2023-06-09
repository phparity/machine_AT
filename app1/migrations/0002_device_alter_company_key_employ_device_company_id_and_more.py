# Generated by Django 4.2 on 2023-04-24 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Device",
            fields=[
                ("device_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("IP", models.CharField(max_length=100)),
                ("port", models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name="company",
            name="key",
            field=models.CharField(
                default="dntszwfaufzkkuo", max_length=100, unique=True
            ),
        ),
        migrations.CreateModel(
            name="Employ",
            fields=[
                ("employ_id", models.AutoField(primary_key=True, serialize=False)),
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
        migrations.AddField(
            model_name="device",
            name="company_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app1.company"
            ),
        ),
        migrations.CreateModel(
            name="Attandance",
            fields=[
                ("attandance_id", models.AutoField(primary_key=True, serialize=False)),
                ("Date", models.CharField(max_length=20)),
                ("time", models.CharField(max_length=20)),
                ("Date_Time", models.CharField(max_length=20)),
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
