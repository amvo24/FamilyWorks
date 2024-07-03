from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from task.models import Task

User = get_user_model()

# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    # might need to make this a generic realtionship

    def __str__(self):
        return f"Comment by {self.user} on {self.task}"
