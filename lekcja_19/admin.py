from django.contrib import admin
from .models import Product
from .models import Customer
from .models import Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id", 
        "name", 
        "description", 
        "price",  
        "quantity",
        "is_available",
        "available_since",
        "created_at",
        "updated_at")
    search_fields = ("name", )
    list_filter = ("created_at", "is_available",)
# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "registered_at",
        "birth_date",
        "is_vip",
        "notes")
    search_fields = ("last_name", "email", )
    list_filter = ("registered_at", )

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "order_number",
        "created_at",
        "is_express",
        "status")
    search_fields = ("order_number", "status", )
    list_filter = ("order_number", "status", )

