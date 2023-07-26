from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'phone_number', 'photo', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')
        user = CustomUser.objects.filter(phone_number=phone_number).first()

        if user is not None:
            raise serializers.ValidationError(
                'User with this phone number already exists.')

        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            phone_number=validated_data['phone_number'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        phone_number = data.get('phone_number')
        password = data.get('password')
        user = CustomUser.objects.filter(phone_number=phone_number).first()

        if user is not None and user.check_password(password):
            return user

        additional_info = {
            'user_exists': user is not None,
            'password_match': user.check_password(password) if user else None,
        }

        raise serializers.ValidationError(
            {
                'error': 'Invalid phone number or password.',
                'additional_info': additional_info,
            }
        )
