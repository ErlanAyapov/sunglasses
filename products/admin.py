from django.contrib import admin
from .models import Product, Customer, Order, Category, Cart


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Cart)