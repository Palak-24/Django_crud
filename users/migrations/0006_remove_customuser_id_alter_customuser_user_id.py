# Generated by Django 5.0.6 on 2024-07-18 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_customuser_user_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="id",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]