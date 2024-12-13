from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics, status
from django.core.cache import cache
from django_app.models.tweet.tweet import Tweet
from django_app.models.tweet.comment import Comment
from django_app.models.tweet.like import Like
from django.core.serializers import serialize
import json



class TweetExplore(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'tweet_explore.html'

    def get(self, request):
        cache_get = cache.get('all_tweets')

        if cache_get is None:
            data = Tweet.objects.all().order_by('-created_at')
            tweet_list = serialize('json', data)
            cache.set('all_tweets', tweet_list, timeout=60*3) 

            tweets = json.loads(tweet_list) 

            return Response({'data': tweets}, status=status.HTTP_200_OK)
        
        tweets = json.loads(cache_get)
        return Response({'data': tweets}, status=status.HTTP_200_OK)


            

        

            
            

    
