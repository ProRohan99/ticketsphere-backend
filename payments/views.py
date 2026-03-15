from rest_framework.viewsets import ModelViewSet
from .models import Payment
from .serializers import PaymentSerializer

# Create your views here.
class PaymentSerializer(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    

