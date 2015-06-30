# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('acc_num', models.AutoField(primary_key=True, serialize=False)),
                ('balance', models.IntegerField()),
                ('open_balance', models.IntegerField(default=500)),
                ('date_opened', models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 30, 9, 45, 6, 825271))),
                ('acc_type', models.CharField(null=True, max_length=20, choices=[('SAVINGS', 'savings'), ('CURRENT', 'current'), ('FIXED', 'fixed')])),
                ('acc_pwd', models.CharField(max_length=20)),
                ('acc_pwd_one', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(null=True, max_length=20)),
                ('last_name', models.CharField(null=True, max_length=20)),
                ('address', models.TextField(null=True, max_length=40)),
                ('cust_mail', models.EmailField(null=True, max_length=40)),
                ('city', models.CharField(null=True, max_length=15)),
                ('state', models.CharField(null=True, max_length=10)),
                ('phone', models.BigIntegerField(null=True, default=0)),
                ('ssn', models.IntegerField(null=True, default=0)),
                ('join_date', models.DateTimeField(editable=False, default=datetime.datetime(2015, 6, 30, 9, 45, 6, 824622))),
                ('login_name', models.CharField(unique=True, max_length=20)),
                ('login_pwd', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('acc_number', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('cur_bal', models.IntegerField()),
                ('trans_date', models.DateTimeField(auto_now_add=True)),
                ('acc_for', models.ManyToManyField(to='bank.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='account',
            name='cust_for',
            field=models.ManyToManyField(to='bank.Customer'),
            preserve_default=True,
        ),
    ]
