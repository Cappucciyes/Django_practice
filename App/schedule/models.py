import uuid
from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Schedule(models.Models):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    title = models.CharField(max_length=255)
    
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='schedule',
    )

    what = models.TextField()

    when = models.DateTimeField()