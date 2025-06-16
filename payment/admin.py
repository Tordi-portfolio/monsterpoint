from django.contrib import admin
from .models import ShippingAddress, OrderItem, Order
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Order)


# create an order inline
class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 0


# extends our order model
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ['date_ordered']
    fields = ['user', 'full_name', 'email', 'shipping_address1', 'amount_paid', 'date_ordered', 'shipped', 'date_shipped']
    inlines = [OrderItemInline]

# Unregister order model
admin.site.unregister(Order)

# Re-register our order model and OrderAdmin
admin.site.register(Order, OrderAdmin)