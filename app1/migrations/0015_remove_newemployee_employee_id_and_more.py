# Generated by Django 4.2 on 2023-04-29 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0014_newemployee_employee_attandance"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newemployee",
            name="employee_id",
        ),
        migrations.AlterField(
            model_name="employee",
            name="card_no",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
