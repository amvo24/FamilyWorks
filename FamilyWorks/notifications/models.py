from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Notificatiions(models.Model):
    NOTIFICATION_TYPES = [
        ('INVITE', 'Invitation'),
        ('TASK', 'Task Update'),
        ('COMMENT', 'Comment')
    ]

    recepient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent-notifications')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)
    content = models.TextField()
