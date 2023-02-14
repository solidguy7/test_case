from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    class Status(models.TextChoices):
        RESOLVED = 'Resolved'
        UNRESOLVED = 'Unresolved'
        FROZEN = 'Frozen'

    sender = models.ForeignKey(User, related_name='ticket', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    answer = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.UNRESOLVED)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.subject
