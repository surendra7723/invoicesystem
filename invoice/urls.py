from django.urls import path
from .views import (
    ListInvoice,
    DetailInvoice,
    ListInvoiceItem,
    DetailInvoiceItem
)

urlpatterns = [
    
    path("invoices/<int:pk>/", DetailInvoice.as_view(), name="invoice_detail"),
    path("invoices/", ListInvoice.as_view(), name="invoice_list"),
    
    
    path("invoice-items/<int:pk>/", DetailInvoiceItem.as_view(), name="invoice_item_detail"),
    path("invoice-items/", ListInvoiceItem.as_view(), name="invoice_item_list"),
]
