from django.db import models
from django_app.models.tweet.tweet import Tweet
from django_app.models.tweet.comment import Comment
from django_app.models.user.user import User


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True, blank=True)  
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)  
    is_read = models.BooleanField(default=False) 

    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

