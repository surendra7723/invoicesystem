from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from django.shortcuts import render
from .serializers import InvoiceSerializer,InvoiceItemSerializer,CustomerSerializer
from .models import Invoice,InvoiceItem,Customer


from .models import Invoice

class ListInvoice(ListCreateAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    
class DetailInvoice(RetrieveUpdateDestroyAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    
    
class ListInvoiceItem(ListCreateAPIView):
    queryset=InvoiceItem.objects.all()
    serializer_class=InvoiceItemSerializer
    
class DetailInvoiceItem(RetrieveUpdateDestroyAPIView):
    queryset=InvoiceItem.objects.all()
    serializer_class=InvoiceItemSerializer
    
class ListCustomer(ListCreateAPIView):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer




