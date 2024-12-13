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
from django_app.serializers.tweet.tweet_s import CreateTweetSerializer
from django.utils import timezone
from django_app.serializers.tweet.tweet_s import UserTweetSerializer
import json
from django_app.elasticsearch.user_doc import UserDocument


class UsernameSearch(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'username-search.html'

    def get(self, request):
        username_query = request.GET.get('username', None)

        if not username_query:
            return Response({'Notif': 'Username not found!'}, status=status.HTTP_404_NOT_FOUND)
        
        
        cache_key = f"username-search-{username_query}"
        cache_get = cache.get(cache_key)

        if not cache_get:
            search = UserDocument.search().query('match', username= username_query)
            data = []

            for item in search:
                data.append({
                    'username': item.username,
                    'last_name': item.last_name,
                    'date_joined': item.date_joined
                })

            cache.set(cache_key, data, timeout=60*3)

            return Response({
                'data': data,
                'username_query': username_query
                }, status=status.HTTP_200_OK)
        
        return Response({'data': cache_get}, status=status.HTTP_200_OK)