from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

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
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    task = models.ForeignKey('task.Task', on_delete=models.CASCADE, null=True, blank=True)
    family = models.ForeignKey('family.Family', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f"Notification for {self.recipient} - {self.notification_type}"
