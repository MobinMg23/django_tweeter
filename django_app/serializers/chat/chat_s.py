from rest_framework import serializers
from django_app.models.message.message import Message


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source='sender.username')
    
    class Meta:
        
        model = Message
        fields = ['id', 'sender', 'sender_username', 'room_name', 'content', 'timestamp']