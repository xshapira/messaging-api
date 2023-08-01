from django.urls import path

from conversations.views import (
    MessageCreate,
    MessageDetail,
    MessageList,
    UnreadMessageList,
)

urlpatterns = [
    path("", MessageList.as_view(), name="message_list"),
    path("create/", MessageCreate.as_view(), name="message_create"),
    path("unread/", UnreadMessageList.as_view(), name="unread_message_list"),
    path("<int:pk>/", MessageDetail.as_view(), name="message_detail"),
]
