from django.db import models
from django.conf import settings

# Create your models here.

User = settings.AUTH_USER_MODEL

class Event(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    location = models.CharField(max_length=200)

    event_date = models.DateTimeField()

    total_seats = models.IntegerField()

    available_seats = models.IntegerField()

    price = models.DecimalField(max_digits=8, decimal_places=2)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)