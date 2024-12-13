from django.urls import re_path
from .consumers import FollowConsumer

websocket_urlpatterns = [
    re_path(r'ws/follow/(?P<user_id>\d+)/$', FollowConsumer.as_asgi()),
]
