# Generated by Django 5.0.6 on 2024-07-18 07:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_remove_customuser_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="user_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
