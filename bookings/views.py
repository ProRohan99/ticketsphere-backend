from rest_framework.viewsets import ModelViewSet
from .model import Booking
from .serializers import BookingSerializer

# Create your views here.
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer