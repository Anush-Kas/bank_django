# Generated by Django 4.2.11 on 2024-03-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bank",
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
                (
                    "name",
                    models.CharField(max_length=200, verbose_name="Name of the bank"),
                ),
                (
                    "min_client_deposit",
                    models.IntegerField(verbose_name="Min client deposit"),
                ),
            ],
        ),
    ]
