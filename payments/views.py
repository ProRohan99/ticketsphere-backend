from rest_framework.viewsets import ModelViewSet
from .models import Payment
from .serializers import PaymentSerializer

# Create your views here.
class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    

