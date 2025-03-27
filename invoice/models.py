from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.core.validators import MinValueValidator
from .constants import CompanyChoices, InvoiceStatus, ProductCategory

class Company(models.Model):

    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    size = models.CharField(max_length=50)
    total_employee = models.PositiveIntegerField() 
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    category = models.CharField(max_length=50,choices=CompanyChoices.COMPANY_CATEGORIES)
    

class Customer(AbstractUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    
    def __str__(self):
        return self.full_name
    
    
class Invoice(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)    
    date_created = models.DateTimeField(auto_now_add=True)
    # total_amount=models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.0)],default=0)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, default=1)  # Assuming '1' is a valid Company ID
    status = models.CharField(max_length=50,choices=InvoiceStatus.INVOICE_STATUSES,default=InvoiceStatus.PENDING)
    
    def __str__(self):
        return f"Invoice of {self.customer.full_name} having ID:{self.id}"


    
    
class InvoiceItem(models.Model):
    invoice=models.ForeignKey(Invoice,on_delete=models.CASCADE,related_name='items')
    item_name=models.CharField(max_length=150)
    quantity=models.PositiveBigIntegerField()
    unit_price=models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.0)])
    
    @property
    def total_price_of_item(self):
        return self.quantity*self.unit_price
    def __str__(self):
        return f"{self.quantity} - {self.unit_price}"

class Product(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.0)])
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    category=models.CharField(max_length=50,choices=ProductCategory.PRODUCT_CATEGORIES)
    
    def __str__(self):
        return self.name






