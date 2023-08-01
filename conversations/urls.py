from django.urls import path

from conversations.views import (
    MessageCreate,
    MessageDetail,
    MessageList,
    UnreadMessageList,
)

urlpatterns = [
    path("messages/", MessageList.as_view(), name="message_list"),
    path("messages/create/", MessageCreate.as_view(), name="message_create"),
    path("messages/unread/", UnreadMessageList.as_view(), name="unread_message_list"),
    path("messages/<int:pk>/", MessageDetail.as_view(), name="message_detail"),
]
