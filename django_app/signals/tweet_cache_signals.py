from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from django.dispatch import receiver
from django.core.serializers import serialize
from django_app.models.tweet.tweet import Tweet
from django_app.models.tweet.comment import Comment
from django_app.serializers.tweet.tweet_s import UserTweetSerializer, CreateTweetSerializer
from django_app.serializers.tweet.comment_s import CommentSerializer



@receiver(post_save, sender=Tweet)
@receiver(post_delete, sender=Tweet)
def update_user_tweet_cache(sender, instance, **kwargs):

    cache_key = f'user-tweets-{instance.user.id}'
    tweets = Tweet.objects.filter(user=instance.user)
    serializer = UserTweetSerializer(tweets, many=True)
    data = serializer.data
    cache.set(cache_key, data, timeout=60*3)


@receiver(post_save, sender=Tweet)
@receiver(post_delete, sender=Tweet)
def explore_tweet_cache(sender, instance, **kwargs):

    tweets = Tweet.objects.all().order_by('-created_at')
    data = serialize('json', tweets)
    cache.set('all_tweets', data, timeout=60*3)


@receiver(post_save, sender=Comment)
@receiver(post_delete, sender=Comment)
def update_user_tweet_comment(sender, instance, **kwargs):

    cache_key = f'comments_{instance.tweet.id}'
    cm = Comment.objects.filter(tweet__id=id).order_by('-created_at')
    comments = CommentSerializer(cm, many=True).data
    cache.set(cache_key, comments, timeout=60*3)

