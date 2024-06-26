# Generated by Django 4.2.11 on 2024-03-12 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("bank", "0005_alter_accountant_bank_alter_client_bank_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="bank",
            name="director",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="banks",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
