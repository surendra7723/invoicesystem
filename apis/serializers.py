from rest_framework import serializers
from invoice.models import Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    multiple_total_amount=serializers.SerializerMethodField()
    
    
    

    
    class Meta:
        
        model=Invoice
        fields=("id","date","total_amount","customer_name",'multiple_total_amount')
    

        