from django.urls import path
from django_app.websockets.follow_consumers import FollowConsumer
from django_app.websockets.chat_consumer import ChatConsumer

websocket_urlpatterns = [
    path('ws/follow/<int:user_id>/', FollowConsumer.as_asgi()),
    path('ws/chat/<str:room_name>/', ChatConsumer.as_asgi()),
]