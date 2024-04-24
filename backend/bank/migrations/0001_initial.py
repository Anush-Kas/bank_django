# Generated by Django 4.2.11 on 2024-04-06 11:56

from django.db import migrations, models
import django.db.models.deletion


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
        migrations.CreateModel(
            name="BankUsers",
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
                    "bank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bank_users",
                        to="bank.bank",
                    ),
                ),
            ],
        ),
    ]
