from django.contrib.auth.models import User
from rest_framework import serializers


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        read_only_fields = ["token"]
        # password and token won't be exposed in any response
        extra_kwargs = {
            "password": {"write_only": True},
            "token": {"write_only": True},
        }

    def create(self, validated_data: dict[str, str]) -> User:
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]
