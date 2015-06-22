# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_auto_20150622_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(null=True, max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(null=True, max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='cust_mail',
            field=models.EmailField(null=True, max_length=40),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(null=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(null=True, max_length=10),
            preserve_default=True,
        ),
    ]
