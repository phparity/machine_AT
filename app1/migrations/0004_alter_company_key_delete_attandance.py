# Generated by Django 4.2 on 2023-04-24 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0003_alter_company_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="company",
            name="key",
            field=models.CharField(
                blank=True,
                help_text="If you not Enter Key It Take Autometicaly",
                max_length=100,
                unique=True,
            ),
        ),
        migrations.DeleteModel(
            name="Attandance",
        ),
    ]
