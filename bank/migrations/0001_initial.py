# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('acc_num', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField(null=True, default=0)),
                ('open_balance', models.IntegerField(null=True, default=0)),
                ('date_opened', models.DateTimeField()),
                ('acc_type', models.CharField(max_length=20, null=True)),
                ('acc_pwd', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('address', models.TextField(max_length=40, null=True)),
                ('cust_mail', models.EmailField(max_length=40, null=True)),
                ('city', models.CharField(max_length=15, null=True)),
                ('state', models.CharField(max_length=10, null=True)),
                ('phone', models.BigIntegerField(null=True, default=0)),
                ('ssn', models.IntegerField(null=True, default=0)),
                ('join_date', models.DateTimeField()),
                ('login_name', models.CharField(max_length=20, unique=True)),
                ('login_pwd', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('amount', models.IntegerField()),
                ('trans_date', models.DateTimeField()),
                ('acc_for', models.ForeignKey(to='bank.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='account',
            name='cust_for',
            field=models.ForeignKey(to='bank.Customer'),
            preserve_default=True,
        ),
    ]
