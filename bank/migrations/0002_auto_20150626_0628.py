# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='date_opened',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 26, 6, 28, 32, 675706)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='open_balance',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='join_date',
            field=models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 26, 6, 28, 32, 675112)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='trans_date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
