# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email_id',
            field=models.CharField(max_length=50),
        ),
    ]
