# Generated by Django 4.2 on 2023-04-26 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0007_attandance"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="employ",
            name="device_id",
        ),
        migrations.DeleteModel(
            name="Attandance",
        ),
        migrations.DeleteModel(
            name="Employ",
        ),
    ]