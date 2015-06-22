# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0008_auto_20150622_0636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='join_date',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.IntegerField(null=True, default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='ssn',
            field=models.IntegerField(null=True, default=0),
            preserve_default=True,
        ),
    ]
