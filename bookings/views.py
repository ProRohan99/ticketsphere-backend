from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .model import Booking
from .serializers import BookingSerializer

# Create your views here.
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    
def perform_create(self, serializer):

    event = serializer.validated_data['event']
    tickets_requested = serializer.validated_data['tickets']

    if event.available_tickets < tickets_requested:
        raise Exception("Not enough tickets available")

    event.available_tickets -= tickets_requested
    event.save()

    serializer.save(user=self.request.user)
    
@api_view(['GET'])
def booking_history(request):

    bookings = Booking.objects.filter(user=request.user)
    serializer = BookingSerializer(bookings, many=True)

    return Response(serializer.data)