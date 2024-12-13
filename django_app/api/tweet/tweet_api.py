from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import CreateAPIView, GenericAPIView, ListAPIView, UpdateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_app.models.user.user import User
from django_app.models.tweet.tweet import Tweet
from django_app.serializers.tweet.tweet_s import CreateTweetSerializer
from django.utils import timezone
from django_app.serializers.tweet.tweet_s import UserTweetSerializer
import json
from django_app.elasticsearch.tweet_doc import TweetDocument


class CreateTweet(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateTweetSerializer
    queryset = Tweet.objects.all()
    
    def post(self, request):
        serializer = self.serializer_class(data=request.POST)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            
            return Response({"message": "Tweet created successfully!"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTweet(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'my-tweets.html'

    def get(self, request):
        cache_key = f'user-tweets-{request.user.id}'
        data = cache.get(cache_key)

        if not data:
            data = []

            return Response({'data': data})
        
        return Response({'data': data}) # Set Cache For signals


class DeleteTweet(APIView):
    permission_classes = (IsAuthenticated,)
 
    def post(self, request, id):
        tweet = get_object_or_404(Tweet, id=id, user=request.user)
        
        if tweet:
            tweet.delete()
            return Response({f'tweet id= {id} -> deleted'})


class EditeTweet(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'edite-tweet.html'

    def get(self, request, id):
        tweet = get_object_or_404(Tweet ,id=id, user=request.user)
        serializer = CreateTweetSerializer(instance=tweet)
        
        return Response({
            'serializer': serializer,
            'data': serializer.data,
            'tweet': tweet
        }, status=status.HTTP_200_OK)
    
    def post(self, request, id):
        tweet = get_object_or_404(Tweet, id=id, user=request.user)
        serializer = CreateTweetSerializer(instance=tweet ,data=request.data)
        
        if serializer.is_valid():
            serializer.save()

            return Response({
            'detail': 'Tweet updated successfully!',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    