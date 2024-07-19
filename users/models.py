from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)

class profile(models.Model):
    profile_id = models.OneToOneField(CustomUser,primary_key=True,on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    location=models.CharField(max_length=30,blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.profile_id.username
