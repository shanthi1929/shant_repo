# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20150625_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 12, 46, 6, 119827)),
            preserve_default=True,
        ),
    ]
