from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.validators import MinValueValidator

class Customer(AbstractUser):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    
    
    def __str__(self):
        return self.full_name
    
    
    
    

# Create your models here.
class Invoice(models.Model):
    
    date_created=models.DateTimeField(auto_now_add=True)
    # total_amount=models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.0)],default=0)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Invoice of {self.customer.full_name} having ID:{self.id}"
    # @property
    # def total_amount(self):
    #     return 


    
    
class InvoiceItem(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='items')
    item_name=models.CharField(max_length=150)
    quantity=models.PositiveBigIntegerField()
    unit_price=models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.0)])
    # total_amount=models.ForeignKey(Invoice,on_delete=models.CASCADE)
    
    @property
    def total_price_of_item(self):
        return self.quantity*self.unit_price
    def __str__(self):
        return f"{self.quantity} - {self.unit_price}"
    
    
    
    
    
  
