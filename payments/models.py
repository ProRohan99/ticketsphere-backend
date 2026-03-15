from django.db import models
from bookings.models import Booking

# Create your models here.

class Payment(models.Model):

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)

    status = models.CharField(max_length=20)

    transaction_id = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)