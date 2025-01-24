from django.shortcuts import render
from invoice.models import Invoice,InvoiceItem
from .serializers import InvoiceSerializer
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin


class InvoiceApiView(GenericAPIView, ListModelMixin):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    
class InvoiceDetailView(generics.RetrieveAPIView):
    queryset=Invoice.objects.all()
    serializer_class=InvoiceSerializer
    
    

# Create your views here.
