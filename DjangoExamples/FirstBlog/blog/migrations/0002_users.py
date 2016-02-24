# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=30)),
                ('contact_no', models.IntegerField()),
                ('password', models.CharField(max_length=30)),
                ('email_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
            ],
        ),
    ]
