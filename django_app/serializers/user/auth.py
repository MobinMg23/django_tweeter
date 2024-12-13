from rest_framework import serializers
from django_app.models.user.user import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # فقط در هنگام نوشتن (ثبت نام) قابل دسترسی است.

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)  # خود Django هش رمز عبور را مدیریت می‌کند
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError("this user is not active")
                data['user'] = user
            else:
                raise serializers.ValidationError("username or password is invalid")
        else:
            raise serializers.ValidationError('username and passwprd necessary')    

        return data