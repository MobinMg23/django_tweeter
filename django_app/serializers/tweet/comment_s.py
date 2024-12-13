from rest_framework import serializers
from django_app.models.tweet.comment import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'user', 'created_at')