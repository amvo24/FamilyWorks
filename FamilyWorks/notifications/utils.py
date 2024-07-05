from django.contrib.auth import get_user_model
from .models import Notifications

User = get_user_model()

def create_notification(user_id, content):
    try:
        user = User.objects.get(id=user_id)
        Notifications.objects.create(user=user, content=content)
    except User.DoesNotExist:
        pass
