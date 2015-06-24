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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('acc_num', models.IntegerField(default=0)),
                ('balance', models.IntegerField(default=0)),
                ('open_balance', models.IntegerField(default=0)),
                ('date_opened', models.DateTimeField(auto_now_add=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('first_Name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('address', models.TextField(max_length=40, null=True)),
                ('cust_mail', models.EmailField(max_length=40, null=True)),
                ('city', models.CharField(max_length=15, null=True)),
                ('state', models.CharField(max_length=10, null=True)),
                ('phone', models.BigIntegerField(default=0, null=True)),
                ('ssn', models.IntegerField(default=0, null=True)),
                ('join_date', models.DateTimeField(default=datetime.datetime(2015, 6, 23, 12, 14, 7, 186754))),
                ('login_name', models.CharField(max_length=20)),
                ('login_pwd', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('amount', models.IntegerField()),
                ('trans_date', models.DateTimeField(auto_now_add=True)),
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
