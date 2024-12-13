from django.urls import path, include
from django_app.api.tweet.tweet_api import CreateTweet, UserTweet, DeleteTweet, EditeTweet
from django_app.api.elastic.tweet_search import TweetSearch
from django_app.api.tweet.comment_api import AddComment, CommentsForPerTweet, DeleteComment
from django_app.api.tweet.like_api import AddLike 
from django_app.api.tweet.explore_api import TweetExplore


urlpatterns = [
    # For Tweet
    path('create-tweet/', CreateTweet.as_view(), name='post'),
    path('my-tweets/', UserTweet.as_view(), name='my-tweets'),
    path('delete-tweet/<int:id>/', DeleteTweet.as_view(), name='delete-tweet'),
    path('edite-tweet/<int:id>/', EditeTweet.as_view(), name='edite-tweet'),

    # For Comment
    path('tweet-comment-add/<int:id>/', AddComment.as_view(), name='add_comment'),
    path('tweet-comments/<int:id>/', CommentsForPerTweet.as_view(), name='comments_for_tweet'),
    path('comment-delete/<int:id>/', DeleteComment.as_view(), name='delete_comment'),
    
    # For Search Tweet
    path('search/hashtag/', TweetSearch.as_view(), name='search_hashtags'),

    # For LIke
    path('tweet-like/<int:id>/', AddLike.as_view(), name='add_like'),

    # For Explore
    path('explore/', TweetExplore.as_view(), name='tweet_explore'),
]