from django.db import models


# Create your models here.
class Products(models.Model):
    productCode = models.CharField(max_length=15,primary_key=True)
    productName=models.CharField(max_length=70)
    productVendor=models.CharField(max_length=50)
    productDescription=models.TextField()
    quantityInstock=models.IntegerField()
    buyPrice=models.IntegerField()
    
    def __unicode__(self):
        return self.productName
    
class Customers(models.Model):
    customersNumber=models.IntegerField(primary_key=True)
    customersName=models.CharField(max_length=50)
    customersPhone=models.IntegerField()
    customersAddress=models.TextField()
    customersCity=models.CharField(max_length=20)
    customerEmail=models.EmailField()
    
    def __unicode__(self):
        return unicode (self.customersNumber)
    
class Orders(models.Model):
    orderNumber=models.IntegerField(primary_key=True)
    oderDate=models.DateField()
    shippedDate=models.DateField()
    oderStatus=models.CharField(max_length=50)
    customersNumber=models.ForeignKey(Customers,verbose_name="customerNumber")
    
    def __unicode__(self):
        return unicode(self.orderNumber)
    
class Orderdetails(models.Model):
    orderNumber=models.ManyToManyField(Orders)
    productCode=models.ForeignKey(Products,verbose_name="productCode")
    quantityOrdered=models.IntegerField()
    priceEach=models.IntegerField()
   
    def __unicode__(self):
        return unicode(self.orderNumber)

class Payments(models.Model):
    customerNumber=models.ManyToManyField(Customers)
    checkNumber=models.IntegerField()
    paymentDate=models.DateField()
    amount=models.FloatField()
    
    def __unicode__(self):
        return unicode(self.customerNumber)
    
    
    
    
    
    
    