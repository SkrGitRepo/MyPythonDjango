# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USER_TABLE',
            fields=[
                ('userid', models.IntegerField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=64)),
                ('typeofuser', models.IntegerField()),
                ('subtypeofuser', models.IntegerField()),
                ('userdescription', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'user_table',
                'managed': False,
            },
        ),
    ]
