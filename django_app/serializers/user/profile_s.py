from rest_framework import serializers
from django_app.models.user.profile import  Profile


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'gender', 'bio')


class EditeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'gender', 'bio')