# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_Name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='customer',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 25, 9, 57, 45, 746846)),
            preserve_default=True,
        ),
    ]
