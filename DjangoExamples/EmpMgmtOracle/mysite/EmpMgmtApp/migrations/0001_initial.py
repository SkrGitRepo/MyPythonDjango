# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoCustomers',
            fields=[
                ('customer_id', models.FloatField(serialize=False, primary_key=True)),
                ('cust_first_name', models.CharField(max_length=20)),
                ('cust_last_name', models.CharField(max_length=20)),
                ('cust_street_address1', models.CharField(max_length=60, null=True, blank=True)),
                ('cust_street_address2', models.CharField(max_length=60, null=True, blank=True)),
                ('cust_city', models.CharField(max_length=30, null=True, blank=True)),
                ('cust_state', models.CharField(max_length=2, null=True, blank=True)),
                ('cust_postal_code', models.CharField(max_length=10, null=True, blank=True)),
                ('phone_number1', models.CharField(max_length=25, null=True, blank=True)),
                ('phone_number2', models.CharField(max_length=25, null=True, blank=True)),
                ('credit_limit', models.DecimalField(null=True, max_digits=9, decimal_places=2, blank=True)),
                ('cust_email', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'db_table': 'demo_customers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DemoOrderItems',
            fields=[
                ('order_item_id', models.IntegerField(serialize=False, primary_key=True)),
                ('unit_price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('quantity', models.IntegerField()),
            ],
            options={
                'db_table': 'demo_order_items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DemoOrders',
            fields=[
                ('order_id', models.FloatField(serialize=False, primary_key=True)),
                ('order_total', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('order_timestamp', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'demo_orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DemoProcudtInfo',
            fields=[
                ('product_id', models.FloatField(serialize=False, primary_key=True)),
                ('product_name', models.CharField(max_length=50, null=True, blank=True)),
                ('product_description', models.CharField(max_length=2000, null=True, blank=True)),
                ('category', models.CharField(max_length=30, null=True, blank=True)),
                ('product_avail', models.CharField(max_length=1, null=True, blank=True)),
                ('list_price', models.DecimalField(null=True, max_digits=8, decimal_places=2, blank=True)),
                ('product_image', models.BinaryField(null=True, blank=True)),
                ('mimetype', models.CharField(max_length=255, null=True, blank=True)),
                ('filename', models.CharField(max_length=400, null=True, blank=True)),
                ('image_last_update', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'demo_procudt_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DemoStates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('st', models.CharField(max_length=30, null=True, blank=True)),
                ('state_name', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'db_table': 'demo_states',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DemoUsers',
            fields=[
                ('user_id', models.FloatField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=100, null=True, blank=True)),
                ('password', models.CharField(max_length=4000, null=True, blank=True)),
                ('created_on', models.DateField(null=True, blank=True)),
                ('quota', models.FloatField(null=True, blank=True)),
                ('products', models.CharField(max_length=1, null=True, blank=True)),
                ('expires_on', models.DateField(null=True, blank=True)),
                ('admin_user', models.CharField(max_length=1, null=True, blank=True)),
            ],
            options={
                'db_table': 'demo_users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(serialize=False, primary_key=True)),
                ('dname', models.CharField(max_length=14, null=True, blank=True)),
                ('loc', models.CharField(max_length=13, null=True, blank=True)),
            ],
            options={
                'db_table': 'dept',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('empno', models.IntegerField(serialize=False, primary_key=True)),
                ('ename', models.CharField(max_length=10, null=True, blank=True)),
                ('job', models.CharField(max_length=9, null=True, blank=True)),
                ('hiredate', models.DateField(null=True, blank=True)),
                ('sal', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('comm', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'emp',
                'managed': False,
            },
        ),
    ]
