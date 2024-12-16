from django.urls import path
from django_app.api.chat.chat_api import ChatRoomMessage

urlpatterns = [
    path('chat/history/<str:room_name>/', ChatRoomMessage.as_view(), name='chat-history'),
]