from rest_framework.viewsets import ModelViewSet
from .models import Event
from .serializers import EventSerializer

# Create your views here.
class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer