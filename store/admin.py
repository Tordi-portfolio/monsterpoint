from django.contrib import admin
from .models import Product, Customer, Order, Category, Profile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Profile)


# Mix profile info with user info
class ProfileInline(admin.StackedInline):
    model = Profile

# Extends user models
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]


# Register the old way
admin.site.unregister(User)

# Register the new way
admin.site.register(User, UserAdmin)