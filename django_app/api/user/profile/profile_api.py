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
from django_app.models.user.profile import Profile
from django_app.serializers.user.profile_s import ProfileCreateSerializer, EditeProfileSerializer
from django.utils import timezone
import json


class ProfileCreate(generics.GenericAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ProfileCreateSerializer
    queryset = Profile.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.POST)
        
        if serializer.is_valid():
            serializer.save(user=request.user)
            
            return Response({'notif': 'profile created is successful!'}, status=status.HTTP_201_CREATED)
        
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class EditeProfile(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'edite-profile.html'

    def get(self, request):
        user = get_object_or_404(Profile, user=request.user)
        serializer = EditeProfileSerializer(instance=user)
        
        return Response({'serializer': serializer.data})

    def post(self, request):
        user = get_object_or_404(Profile, user=request.user)
        serializer = EditeProfileSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            return Response({'notif': 'profile edite successfuly!'}, status=status.HTTP_200_OK)
        
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


