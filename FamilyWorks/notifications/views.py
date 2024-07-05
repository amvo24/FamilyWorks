from rest_framework import viewsets
from .models import Notifications

# Create your views here.
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    
