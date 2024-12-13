from rest_framework import serializers
from django_app.models.tweet.tweet import Tweet


class CreateTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('content', 'hashtag')


class UserTweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['id', 'user', 'content', 'created_at', 'updated_at', 'hashtag']

    
