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
from django_app.elasticsearch.tweet_doc import TweetDocument



class TweetSearch(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'hashtag-search.html'

    def get(self, request):
        hashtag_query = request.GET.get('hashtag', None)

        if not hashtag_query:
            return Response({'error': 'Hashtag is None'}, status=status.HTTP_400_BAD_REQUEST)

        if not hashtag_query.startswith('#'):
            hashtag_query = f"#{hashtag_query}"

        cache_key = f"hashtag-search-{hashtag_query}"
        cache_get = cache.get(cache_key)
        
        if not cache_get:
            search = TweetDocument.search().query('match', hashtag=hashtag_query)
            data = []
            for item in search:

                data.append({
                    "content": item.content,
                    "hashtag": item.hashtag,
                    "created_at": item.created_at
                })

            cache.set(cache_key, data, timeout=60*3)

            return Response({"results": data, "hashtag_query": hashtag_query})
        
        return Response({"results": cache_get, "hashtag_query": hashtag_query})