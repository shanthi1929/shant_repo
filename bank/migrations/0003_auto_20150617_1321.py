# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_customer_pwd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='interest',
        ),
        migrations.AddField(
            model_name='account',
            name='acc_type',
            field=models.CharField(null=True, max_length=20),
            preserve_default=True,
        ),
    ]
