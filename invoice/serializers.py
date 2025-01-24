from rest_framework import serializers
from .models import Customer,Invoice,InvoiceItem

class CustomerSerializer(serializers.ModelSerializer):
    

    class Meta:
        model=Customer
        fields=["email","full_name","email"]        

class InvoiceItemSerializer(serializers.ModelSerializer):

    invoice=serializers.StringRelatedField()
    class Meta:
        model=InvoiceItem
        fields=["id","item_name","quantity","unit_price","invoice"]

class InvoiceSerializer(serializers.ModelSerializer):
    customer=CustomerSerializer()
    items=InvoiceItemSerializer(many=True,read_only=True)
    

    
    class Meta:
        model=Invoice
        fields=["id","date_created",'customer','items']


        
        