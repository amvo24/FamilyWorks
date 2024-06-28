from django.db import models
from django.contrib.auth.models import User, AbstractUser

# For this project we are using Djangos built in user and auth
# functionalities. Therefore we only create the below model to
# inherit the user model because we want to add birthdays as a field.

# Create your models here.
class CustomUser(AbstractUser):
    birthday = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.username

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
