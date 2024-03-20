# Generated by Django 4.2.11 on 2024-03-09 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("bank", "0002_accountant"),
    ]

    operations = [
        migrations.CreateModel(
            name="Manager",
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
                    models.CharField(
                        max_length=200, verbose_name="Name of the manager"
                    ),
                ),
                ("salary", models.IntegerField(default=200, verbose_name="Salary")),
                (
                    "accountant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bank.accountant",
                        verbose_name="Accountant of the manager",
                    ),
                ),
                (
                    "bank",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bank.bank",
                        verbose_name="Bank of the manager",
                    ),
                ),
            ],
        ),
    ]