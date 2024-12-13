from django.db import models 
from django_app.models.user.user import User


class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    hashtag = models.CharField(max_length=20, null=True, blank=True)
    # image = models.ImageField(upload_to='tweets/', blank=True)  

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"
    
    
