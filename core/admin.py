from django.contrib import admin
from core.models import Client, InventoryItem, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "phone", "company", "created_at"]
    search_fields = ["first_name", "last_name"]

@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "quantity", "price", "low_stock_threshold", "created_at"]
    search_fields = ["name"]
    list_filter = ["created_at"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["client", "item", "quantity", "status", "created_at"]
    search_fields = ["client__first_name", "client__last_name"]
    list_filter = ["status", "created_at"]