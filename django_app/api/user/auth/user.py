from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.cache import cache
from django_app.models.user.user import User
from django_app.models.user.follow import Follow
from django_app.serializers.user.auth import SignUpSerializer, LoginSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.tokens import RefreshToken
from allauth.account.views import LogoutView, LoginView
from django.contrib.auth import authenticate
import json


class SignUpAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = SignUpSerializer


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer,]
    template_name = 'Login.html'
    
    def get(self, request):
        serializer = LoginSerializer()
        return Response({
            "serializer": serializer
        })
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)

            request.session['access_token'] = str(refresh.access_token)
            request.session['refresh_token'] = str(refresh)
            
            return Response({
                "serializer": serializer,  # سریالایزر خالی برای رندر دوباره فرم
                "message": "Login successful",
            }, template_name=self.template_name, status=status.HTTP_200_OK)

        return Response({
            'serializer': serializer,
            'message': 'Invalid',
        }, status=status.HTTP_400_BAD_REQUEST)
    
        
class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    def post(self, request):
        try:
            # حذف توکن‌ها از session
            request.session.pop('access_token', None)
            request.session.pop('refresh_token', None)
            return redirect('login')  # بازگشت به صفحه ورود
        except KeyError:
            return Response({'detail': 'Logout failed!'}, status=400)


class UserListAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        data = []

        for user in users:
            is_following = Follow.objects.filter(follower=request.user, followed=user).exists()
            data.append({
                "id": user.id,
                "username": user.username,
                "is_following": is_following
            })

        return Response(data, status=status.HTTP_200_OK)

    






