from django.db import models
from django.conf import settings
from events.models import Event

# Create your models here.

User = settings.AUTH_USER_MODEL

class Booking(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    quantity = models.IntegerField()

    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20, default="Confirmed")

    created_at = models.DateTimeField(auto_now_add=True)
    
    def delete(self, *args, **kwargs):
        # restore seats
        event = self.event
        event.available_seats += self.quantity
        event.save()

        super().delete(*args, **kwargs)