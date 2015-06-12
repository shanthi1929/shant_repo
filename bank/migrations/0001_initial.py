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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('acc_num', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('open_balance', models.IntegerField()),
                ('cust_id', models.IntegerField()),
                ('date_opened', models.DateTimeField(auto_now_add=True)),
                ('interest', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('cust_id', models.IntegerField()),
                ('first_Name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=40)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=10)),
                ('phone', models.IntegerField()),
                ('ssn', models.IntegerField()),
                ('join_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('acc_num', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('transdate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(to='bank.Customer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='transaction',
            field=models.ForeignKey(to='bank.Transaction'),
            preserve_default=True,
        ),
    ]
