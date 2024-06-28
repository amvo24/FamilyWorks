from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]

    # This logic handles hashing the password when a user signs up
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        instance.set_password(password)
        instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            "username": attrs.get("username"),
            "password": attrs.get("password")
        }

        if all(credentials.values()):
            user = authenticate(request=self.context.get('request'), **credentials)

            if user:
                data = super().validate(attrs)
                return data

        raise serializers.ValidationError("Invalid Credentials")
