from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.renderers import TemplateHTMLRenderer
from django.core.cache import cache
from django_app.models.user.user import User


class UserListAPIView(APIView, ):
    permission_classes = (AllowAny,)
    renderer_classes = (TemplateHTMLRenderer,)
    template_name = 'user-list.html'
    
    def get(self, request):
        data = cache.get('user_list')

        if not data:
            data = User.objects.all()

            cache.set('user_list', list(data), timeout=60*3)
            
        return Response({
            'data': data
            })