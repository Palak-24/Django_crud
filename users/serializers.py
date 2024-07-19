
from rest_framework import serializers
from .models import CustomUser,profile
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['user_id', 'username']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=profile
        fields=['profile_id','date_of_birth','height','weight','location']
        
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)
    height = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True, required=False)
    weight = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True, required=False)
    location = serializers.CharField(max_length=100, allow_blank=True, required=False)  

    class Meta:
        model = CustomUser
        fields = ['username', 'password','password_confirm','height','weight','location']

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        profile_data = validated_data.pop('profile', {})
        height = profile_data.pop('height', None)
        weight = profile_data.pop('weight', None)
        location = profile_data.pop('location', None)

        user = CustomUser.objects.create_user(**validated_data, password=password)
        profile.objects.create(profile_id=user,height=height,weight=weight)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if CustomUser:
                data['user'] = user
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")
        return data