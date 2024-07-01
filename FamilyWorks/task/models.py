from django.db import models
from django.contrib.auth import get_user_model
from family.models import Family
from django.utils import timezone

User = get_user_model()

# Create your models here.
class Task(models.Model):
    class StatusChoices(models.TextChoices):
        OPEN = 'open', 'Open'
        IN_PROGRESS = 'in_progress', 'In Progress'
        COMPLETED = 'completed', 'Completed'

    class PriorityChoices(models.TextChoices):
        HIGH = 'high', 'High'
        MEDIUM = 'medium', 'Medium'
        LOW = 'low', 'Low'

    title = models.CharField(max_length=150, null=False)
    description = models.CharField(max_length=225, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='assigned_to')
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.OPEN)
    priority = models.CharField(max_length=20, choices=PriorityChoices.choices, default=PriorityChoices.MEDIUM)

    def __str__(self) -> str:
        return self.title
