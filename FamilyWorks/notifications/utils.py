from django.contrib.auth import get_user_model
from .models import Notifications
from family.models import FamilyMembership

User = get_user_model()

def create_notification(recepient_id, sender_id, notification_type, content, task=None, family=None):
    # try:
        recepient = User.objects.get(id=recepient_id)
        print("THIS IS recepient ", recepient)
        sender = User.objects.get(id=sender_id)
        print("THIS IS sender ", sender)
        Notifications.objects.create(
            recepient=recepient,
            sender=sender,
            notification_type=notification_type,
            content=content,
            task=task,
            family=family
        )
    # except User.DoesNotExist:
    #     print(f"THE NOTIFICATION HIT THE EXCEPT BLOCK")
