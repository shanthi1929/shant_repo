# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20150626_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='date_opened',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 26, 8, 35, 33, 820617), editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 26, 8, 35, 33, 820009), editable=False),
            preserve_default=True,
        ),
    ]
