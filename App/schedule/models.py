import uuid
from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

# Create your models here.
class Schedule(models.Model):
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

    time_created = models.DateTimeField()
    time_edited = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("schedule_detail", kwargs={"pk": self.pk})
    