from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.cache import cache
from django_app.models.user.user import User
from django_app.models.user.follow import Follow
from django.utils import timezone
from django_app.serializers.user.follow_s import FollowSerializer
import json
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer



class FollowAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, id):
        follower = request.user
        followed = get_object_or_404(User, id=id)

        if follower == followed:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follow = Follow.objects.filter(follower=follower, followed=followed).first()

        if follow:
            follow.delete()
            return Response({
                "message": f"You have unfollowed {followed.username}.",
                "action": "unfollow"
            }, status=status.HTTP_200_OK)
        
        followers_count = Follow.objects.filter(followed=followed).count()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'user_{id}_follows',  # گروه مربوط به کاربر هدف
            {
                'type': 'send_follow_update',
                'followers_count': followers_count,
            }
        )

        follow = Follow.objects.create(follower=follower, followed=followed)
        return Response({
            "message": f"You are now following {followed.username}.",
            "action": "follow"
        }, status=status.HTTP_201_CREATED)
