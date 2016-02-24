'''
Created on Oct 13, 2015

@author: sumkuma2
'''
from OrderApp.models import Products


##Inserting data in db
##Products.objects.create(productCode='1111',productName='cable',productVendor='cisco',productDescription='good',quantityInStock='10',buyPrice='1135')

##print Products.objects.all()


##Updating data in table

#p1 = Products.objects.get(productCode='1111')

#print "its prod name is :", p1.productName
#p1.productName = "Computer"
#p1.save()

#print "Order By Product",Products.objects.order_by('productName')

## Filter is like  "LIKE" statement in MySql

#print "Filter by Product",Products.objects.filter(productName__icontains='')

