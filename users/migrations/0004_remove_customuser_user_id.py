# Generated by Django 5.0.6 on 2024-07-18 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_customuser_user_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="user_id",
        ),
    ]