from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid

User = get_user_model()


# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class FamilyMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

class Invitation(models.Model):
    invitation_token = models.UUIDField(unique=True, default=uuid.uuid4)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient')
    recipient_email = models.EmailField()
    expiry_date = models.DateTimeField(default= timezone.now() + timezone.timedelta(days=7))
    accepted = models.BooleanField(null=True, default=None)
