from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Product, Profile, OrderItem, Order


class ProductList(admin.ModelAdmin):
    list_display = ('product_name', 'product_description', 'price')
    list_filter = ('product_name', 'price')
    search_fields = ['product_name']
    ordering = ['product_name']


# Model Registers
admin.site.register(Product, ProductList)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'home_phone', 'addr_line1', 'addr_line2',
                    'addr_line3', 'addr_line4', 'city', 'state',
                    'postal_code']
    list_filter = ['state', 'city']
    search_fields = ['home_phone']


admin.site.register(Profile, ProfileAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city',
                    'created', 'updated']
    list_filter = ['created', 'updated']
    inlines = [OrderItemInline]
