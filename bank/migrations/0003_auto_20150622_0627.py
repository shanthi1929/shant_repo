# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20150618_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_Name',
            field=models.CharField(max_length=20, default=0),
            preserve_default=True,
        ),
    ]
