from rest_framework.viewsets import ModelViewSet
from .models import Event
from .serializers import EventSerializer

# Create your views here.
class EventListAPI(ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()

        category = self.request.query_params.get('category')
        location = self.request.query_params.get('location')

        if category:
            queryset = queryset.filter(category=category)

        if location:
            queryset = queryset.filter(location=location)

        return queryset