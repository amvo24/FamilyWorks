from rest_framework import serializers
from .models import Notifications

class NotificationSerializer(serializers.ModelSerializer):
# All of this is subject to change as I get a clearer understanding of
# how I want this to work.
    class Meta:
        model = Notifications
        fields = [
            'recepient',
            'sender',
            'notification_type',
            'content',
            'seen',
            'created_at',
            'task',
            'family'
        ]
