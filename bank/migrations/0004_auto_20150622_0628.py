# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_auto_20150622_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_Name',
            field=models.CharField(max_length=20, default=True),
            preserve_default=True,
        ),
    ]
