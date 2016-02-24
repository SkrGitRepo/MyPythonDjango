# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class DemoCustomers(models.Model):
    customer_id = models.FloatField(primary_key=True)
    cust_first_name = models.CharField(max_length=20)
    cust_last_name = models.CharField(max_length=20)
    cust_street_address1 = models.CharField(max_length=60, blank=True, null=True)
    cust_street_address2 = models.CharField(max_length=60, blank=True, null=True)
    cust_city = models.CharField(max_length=30, blank=True, null=True)
    cust_state = models.CharField(max_length=2, blank=True, null=True)
    cust_postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone_number1 = models.CharField(max_length=25, blank=True, null=True)
    phone_number2 = models.CharField(max_length=25, blank=True, null=True)
    credit_limit = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    cust_email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_customers'


class DemoOrderItems(models.Model):
    order_item_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey('DemoOrders')
    product = models.ForeignKey('DemoProcudtInfo')
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'demo_order_items'


class DemoOrders(models.Model):
    order_id = models.FloatField(primary_key=True)
    customer = models.ForeignKey(DemoCustomers)
    order_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    order_timestamp = models.DateField(blank=True, null=True)
    user = models.ForeignKey('DemoUsers', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_orders'


class DemoProcudtInfo(models.Model):
    product_id = models.FloatField(primary_key=True)
    product_name = models.CharField(max_length=50, blank=True, null=True)
    product_description = models.CharField(max_length=2000, blank=True, null=True)
    category = models.CharField(max_length=30, blank=True, null=True)
    product_avail = models.CharField(max_length=1, blank=True, null=True)
    list_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    product_image = models.BinaryField(blank=True, null=True)
    mimetype = models.CharField(max_length=255, blank=True, null=True)
    filename = models.CharField(max_length=400, blank=True, null=True)
    image_last_update = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_procudt_info'
    

class DemoStates(models.Model):
    st = models.CharField(max_length=30, blank=True, null=True)
    state_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_states'


class DemoUsers(models.Model):
    user_id = models.FloatField(primary_key=True)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=4000, blank=True, null=True)
    created_on = models.DateField(blank=True, null=True)
    quota = models.FloatField(blank=True, null=True)
    products = models.CharField(max_length=1, blank=True, null=True)
    expires_on = models.DateField(blank=True, null=True)
    admin_user = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demo_users'


class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=14, blank=True, null=True)
    loc = models.CharField(max_length=13, blank=True, null=True)

    def __unicode__(self):
        return unicode (self.deptno)
    class Meta:
        managed = False
        db_table = 'dept'


class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10, blank=True, null=True)
    job = models.CharField(max_length=9, blank=True, null=True)
    mgr = models.ForeignKey('self', db_column='mgr', blank=True, null=True)
    hiredate = models.DateField(blank=True, null=True)
    sal = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    comm = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    deptno = models.ForeignKey(Dept, db_column='deptno', blank=True, null=True)
    
    def __unicode__(self):
        return unicode (self.mgr)


    class Meta:
        managed = False
        db_table = 'emp'
