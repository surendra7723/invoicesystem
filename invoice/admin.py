from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer
from .models import Customer, Invoice, InvoiceItem
from .forms import CustomerCreationForm,CustomerChangeForm

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    add_form=CustomerCreationForm
    form=CustomerChangeForm
    model=Customer
    
    list_display = ('full_name',, 'email','is_staff')  
    search_fields = ('full_name', 'email')      
    list_filter = ('full_name',)  
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)
    
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_created')   
    search_fields = ('customer__full_name',)                        
                    
                                  

@admin.register(InvoiceItem)
class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'item_name', 'quantity', 'unit_price', 'total_price_of_item') 
    search_fields = ('item_name', 'invoice__id')  
                
