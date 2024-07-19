
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
        fields=['profile_id','date_of_birth','height','weight']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)
    date_of_birth = serializers.DateField(required=False, allow_null=True)
    height = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True, required=False)
    weight = serializers.DecimalField(max_digits=5, decimal_places=2, allow_null=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'password_confirm', 'date_of_birth', 'height', 'weight']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')
        
        if password != password_confirm:
            raise serializers.ValidationError({"password_confirm": "Passwords do not match."})
        if not attrs.get('height'):
            raise serializers.ValidationError({"height": "This field is required."})
        
        if not attrs.get('weight'):
            raise serializers.ValidationError({"weight": "This field is required."})
        if not attrs.get("date_of_birth"):
            raise serializers.ValidationError({"date_of_birth": "This field is required."})

        return attrs
     
    def create(self, validated_data):
        validated_data.pop('password_confirm')
        date_of_birth = validated_data.pop('date_of_birth', None)
        height = validated_data.pop('height', None)
        weight = validated_data.pop('weight', None)

        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(validated_data.get('password')) 
        profile.objects.create(
            profile_id=user,
            date_of_birth=date_of_birth,
            height=height,
            weight=weight
        )
        return user

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField(
        required=True,
        error_messages={'required': 'This field is required.'}
    )
    password = serializers.CharField(
        required=True,
        write_only=True,
        error_messages={'required': 'This field is required.'}
    )


    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError({
                'username': 'This field is required.',
                'password': 'This field is required.'
            })

        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError({
                'non_field_errors': 'Invalid username or password.'
            })
        
        attrs['user'] = user
        return attrs