from django.db.models import Q, QuerySet
from rest_framework import generics

from conversations.models import Message
from conversations.serializers import MessageSerializer


class MessageList(generics.ListAPIView):
    """
    List messages.

    get:
    Returns a list of all messages for a specific user.
    """

    serializer_class = MessageSerializer

    def get_queryset(self) -> QuerySet[Message]:
        """
        Filter Messages based on logged in user.

        Returns:
            QuerySet containing Message objects that the logged in user either sent or received.
        """

        user = self.request.user
        return Message.objects.filter(Q(from_user=user) | Q(to_user=user))


class MessageCreate(generics.CreateAPIView):
    """
    Create new messages.
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class UnreadMessageList(generics.ListAPIView):
    """
    List unread received messages for the authenticated user.

    We don't include sent messages, as those cannot be considered unread.
    """

    serializer_class = MessageSerializer

    def get_queryset(self) -> QuerySet[Message]:
        """
        Filter for unread received messages.
        """

        user = self.request.user
        return Message.objects.filter(to_user=user, is_read=False)
