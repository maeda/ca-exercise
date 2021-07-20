import uuid

from django.db import models


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session_id = models.UUIDField()
    category = models.CharField(blank=False, max_length=128)
    name = models.CharField(blank=False, max_length=64)
    data = models.JSONField(blank=False)
    timestamp = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['timestamp']
