from rest_framework import serializers
from django_app.models.user.follow import Follow


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('follower', 'followed', 'created_at')
        