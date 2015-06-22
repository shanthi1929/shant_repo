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
                ('acc_num', models.IntegerField(serialize=False, primary_key=True)),
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
                ('cust_id', models.IntegerField(serialize=False, primary_key=True)),
                ('first_Name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=40)),
                ('cust_mail', models.EmailField(max_length=40, default=0)),
                ('city', models.CharField(max_length=15)),
                ('state', models.CharField(max_length=10)),
                ('phone', models.IntegerField(default=0)),
                ('ssn', models.IntegerField(default=0)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Login_details',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('login_name', models.CharField(max_length=20)),
                ('login_pwd', models.CharField(max_length=20)),
                ('log_for', models.ForeignKey(to='bank.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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
