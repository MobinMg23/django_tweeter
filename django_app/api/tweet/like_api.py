from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.cache import cache
from django_app.models.user.user import User
from django_app.models.tweet.tweet import Tweet
from django_app.models.tweet.like import Like
from django_app.serializers.tweet.comment_s import CommentSerializer
from django.utils import timezone
from django.core.serializers import serialize
import json



class AddLike(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, id):
        tweet = get_object_or_404(Tweet, id=id)
        user_like_for_tweet = Like.objects.filter(tweet=tweet, user=request.user)
        cache_key = f'likes_count_{id}'
        cache_get = cache.get(cache_key)

        if cache_get is None:
            likes_count = Like.objects.filter(tweet__id=id).count()
            cache.set(cache_key, likes_count, timeout=60*3)

        if not user_like_for_tweet.exists():
            Like.objects.create(tweet=tweet, user=request.user)
            cache.incr(cache_key, delta=1)

            return Response({'Notif': 'Like'}, status=status.HTTP_201_CREATED)
            
        else:
            user_like_for_tweet.delete()
            cache.decr(cache_key, delta=1)

            return Response({'Notif': 'UnLike'}, status=status.HTTP_200_OK)
            

                    

            
        

            

                            

            









        
        
