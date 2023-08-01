from rest_framework import serializers

from conversations.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            "from_user",
            "to_user",
            "subject",
            "body",
            "created_at",
            "is_read",
        ]
