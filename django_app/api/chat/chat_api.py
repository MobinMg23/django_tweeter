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
from django_app.models.message.message import Message
from django_app.serializers.chat.chat_s import MessageSerializer

class ChatRoomMessage(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = ''

    def get(self, request, room_name):
        cache_key = f'chat_room_name_{room_name}'
        cache_get = cache.get(cache_key)

        if not cache_get:
            messages = Message.objects.filter(room_name=room_name).order_by('-timestamp')
            serializer = MessageSerializer(messages, many=True)
            cache.set(cache_key, serializer.data, timeout=60*3)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        
        return Response({'data': cache_get}, status=status.HTTP_200_OK)