from django.db import models
import uuid
from django.core.validators import MinValueValidator

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.id})"
    
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    quantity = models.IntegerField()
    is_available = models.BooleanField(default=False)
    available_since = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
    
class Customer(models.Model):
    email = models.EmailField(max_length=254, unique = True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registered_at = models.DateTimeField(auto_now_add = True)
    birth_date = models.DateField(blank = True, null = True) 
    is_vip = models.BooleanField(default=False)
    notes = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Order(models.Model):
    order_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    is_express = models.BooleanField(default=False)

    class Status(models.TextChoices):
        PENDIGN = "pending", "Pending"
        PROCESSING = "processing", "Processing"
        SHIPPED = "shipped", "Shipped"
        CANCELLED = "cancelled", "Cancelled"

    status = models.CharField(
        max_length=15,
        choices = Status.choices,
        default = Status.PENDIGN
    )
    def __str__(self):
        return f"{self.order_number}"
    

    
# Create your models here.
