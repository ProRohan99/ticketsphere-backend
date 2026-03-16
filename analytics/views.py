from rest_framework.views import APIView
from rest_framework.response import Response
from bookings.models import Booking
from events.models import Event
from payments.models import Payment

# Create your views here.

class AnalyticsDashboardAPI(APIView):

    def get(self, request):

        total_events = Event.objects.count()
        total_bookings = Booking.objects.count()
        total_payments = Payment.objects.count()

        data = {
            "total_events": total_events,
            "total_bookings": total_bookings,
            "total_payments": total_payments
        }

        return Response(data)


