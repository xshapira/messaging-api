from django.db.models import Q, QuerySet
from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

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
        Filter Messages based on authenticated user.

        Returns:
            QuerySet containing Message objects that the authenticated user either sent or received.
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


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a message.

    get:
    Retrieve a message by id.

    put:
    Update an existing message.
    Validates and saves updated values to the existing Message.

    delete:
    Delete a message. Removes the Message from the database.
    """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get(self, request: Request, *Args, **kwargs) -> Response:
        """
        Mark the message as read when it's retrieved.

        If the authenticated user is the receiver and the message is unread, it's marked as read.
        """

        response = super().get(request, *Args, **kwargs)
        message = self.get_object()
        if request.user == message.to_user and not message.is_read:
            message.is_read = True
            message.save()
        return response

    def delete(self, request: Request, *args, **kwargs) -> Response:
        """
        Make sure that only the sender or receiver can delete the message.

        If the authenticated user isn't the sender or receiver, a 403 Forbidden response is returned.
        """

        message = self.get_object()
        if request.user not in [message.to_user, message.from_user]:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().delete(request, *args, **kwargs)
