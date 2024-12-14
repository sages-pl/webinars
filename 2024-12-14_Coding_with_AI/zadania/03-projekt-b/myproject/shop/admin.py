from django.contrib import admin
from .models import Customer, Address, Product, Order


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email']
    search_fields = ['^lastname', '=email']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['customer', 'type', 'city', 'postcode']
    autocomplete_fields = ['customer']
    radio_fields = {'type': admin.VERTICAL}
    search_fields = ['customer__firstname', 'customer__lastname', 'city', 'postcode']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'ean13', 'price']
    search_fields = ['^name', '=ean13']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer']
    autocomplete_fields = ['customer', 'product']
    search_fields = ['customer__firstname', 'customer__lastname']
    filter_horizontal = ['product']
