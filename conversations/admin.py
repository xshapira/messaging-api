from django.contrib import admin

from conversations.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "from_user",
        "to_user",
        "subject",
        "created_at",
        "is_read",
    )
