# Generated by Django 5.0.6 on 2024-07-18 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0009_customuser_email_profile_height_profile_weight"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="location",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]