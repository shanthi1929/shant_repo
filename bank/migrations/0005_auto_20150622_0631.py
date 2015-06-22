# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_auto_20150622_0628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True, max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(blank=True, max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='cust_mail',
            field=models.EmailField(blank=True, max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_Name',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(blank=True, max_length=10),
            preserve_default=True,
        ),
    ]
