# Generated by Django 5.0.6 on 2024-07-18 08:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_remove_customuser_id_alter_customuser_user_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="profile",
            fields=[
                (
                    "profile_id",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]