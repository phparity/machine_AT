# Generated by Django 4.2 on 2023-04-29 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0015_remove_newemployee_employee_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newemployee",
            name="card_no",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
