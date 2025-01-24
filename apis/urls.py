from django.urls import path
from .views import InvoiceApiView
urlpatterns=[   
    path("",InvoiceApiView.as_view(),name='invoice_list'),
    
]