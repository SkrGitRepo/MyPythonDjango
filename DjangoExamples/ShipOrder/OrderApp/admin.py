from django.contrib import admin
from OrderApp.models import Products, Customers, Orderdetails, Payments, Orders
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(Orderdetails)
admin.site.register(Payments)


# Register your models here.
