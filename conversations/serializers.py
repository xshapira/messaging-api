from django.contrib.auth.models import User
from rest_framework import serializers

from conversations.models import Message


class UserField(serializers.PrimaryKeyRelatedField):
    """
    Customize the serializer to allow specify users by username instead
    of primary key.
    """

    def to_internal_value(self, data: str) -> User:
        try:
            user = User.objects.get(username=data)
            return user
        except User.DoesNotExist as e:
            raise serializers.ValidationError(f"username {data} does not exist") from e

    def to_representation(self, value: User) -> str:
        """
        Customize the response to include the usernames instead of the
        primary keys.
        """

        user = User.objects.get(pk=value.pk)
        return user.username


class MessageSerializer(serializers.ModelSerializer):
    from_user = serializers.ReadOnlyField(source="from_user.username")
    to_user = UserField(queryset=User.objects.all())

    def create(self, validated_data):
        validated_data["from_user"] = self.context["request"].user
        return super().create(validated_data)

    class Meta:
        model = Message
        read_only_fields = ["from_user"]
        fields = [
            "id",
            "from_user",
            "to_user",
            "subject",
            "body",
            "created_at",
            "is_read",
        ]
