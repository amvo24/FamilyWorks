from rest_framework import viewsets, permissions
from .models import Notifications
from .serializer import NotificationSerializer

# Create your views here.
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notifications.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
