from rest_framework import serializers
from django.db import transaction
from .models import Booking
from events.models import Event


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        quantity = validated_data['quantity']
        event_id = validated_data['event'].id

        with transaction.atomic():
            # lock the event row
            event = Event.objects.select_for_update().get(id=event_id)

            if event.available_seats < quantity:
                raise serializers.ValidationError("Not enough seats available")

            # deduct seats
            event.available_seats -= quantity
            event.save()

            booking = Booking.objects.create(**validated_data)

        return booking
        
    