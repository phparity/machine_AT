# Generated by Django 4.2 on 2023-04-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0002_device_alter_company_key_employ_device_company_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="key",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]