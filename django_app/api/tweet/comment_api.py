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
from django_app.models.tweet.comment import Comment
from django_app.serializers.tweet.comment_s import CommentSerializer
from django.utils import timezone
from django.core.serializers import serialize
import json


class AddComment(APIView):
    permission_classes = (IsAuthenticated,)
    
    def post(self, request, id):
        serializer = CommentSerializer(data=request.data)
        tweet = get_object_or_404(Tweet, id=id)

        if serializer.is_valid():
           comment =  serializer.save(commit=False)
           comment.user = request.user
           comment.tweet = tweet
           comment.save()
           return Response({'detail': 'Comment added'}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CommentsForPerTweet(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        cache_key = f'comments_{id}'
        comments = cache.get(cache_key)
        
        if not comments:
            comments = []

            return Response({"comments": comments})

        return Response({'comments': comments}, status=status.HTTP_200_OK)
        

class DeleteComment(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, id):
        comment = get_object_or_404(Comment, id=id, user=request.user)
        comment.delete()

        return Response({'notif': 'Your comment deleted successfully!'}, status=status.HTTP_200_OK)
        

