from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = '__all__'
        
        
    def validate(self, data):
        user = data['user']
        event = data['event']

        if Booking.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("You have already booked this event.")

        return data