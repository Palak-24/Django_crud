from django.contrib import admin
from django.contrib.auth.models import User
from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)