from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sent_messages"
    )
    to_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="received_messages"
    )
    subject = models.CharField(max_length=120)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
