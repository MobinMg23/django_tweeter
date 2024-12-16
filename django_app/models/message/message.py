from django.db import models
from django_app.models.user.user import User


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    room_name = models.CharField(max_length=100)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} -> {self.recipient}: {self.content[:20]}'
    
    class Meta:
        ordering = ['-timestamp']
