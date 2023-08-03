from django.contrib.auth.models import User
from rest_framework import serializers


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email"]
        # password won't be exposed in any response
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict[str, str]) -> User:
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
