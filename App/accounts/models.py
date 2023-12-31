import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        editable=False,
        default=uuid.uuid4()
    )