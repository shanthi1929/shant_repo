from django.db import models
from django.db.models import permalink
from django.db import IntegrityError


class Customer(models.Model):
    
    cust_id = models.AutoField(primary_key=True)
    first_Name = models.CharField(max_length=20,null=True)
    last_name = models.CharField(max_length=20,null=True)
    address = models.TextField(max_length=40,null=True)
    cust_mail = models.EmailField(max_length=40,null=True)
    city = models.CharField(max_length=15,null=True)
    state = models.CharField(max_length=10,null=True)
    phone = models.IntegerField(default=0,null=True)
    ssn = models.IntegerField(default=0,null=True)
    join_date = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return '%s' % self.cust_id

    
 class Account(models.Model):
    acc_num=models.AutoField(primary_key=True)
    balance=models.IntegerField(default=0)
    open_balance=models.IntegerField(default=0)
    date_opened=models.DateTimeField(auto_now_add=True)
    acc_type=models.CharField(null=True,max_length=20)
    acc_pwd=models.CharField(max_length=20)
    cust_for=models.ForeignKey(Customer)

    def __unicode__(self):
        return '%s' % self.acc_num


class Transaction(models.Model):
    amount=models.IntegerField()
    trans_date=models.DateTimeField(auto_now_add=True)
    acc_for=models.ForeignKey(Account)

    def __unicode__(self):
        return '%s' % self.amount


class Login_details(models.Model):
    login_name=models.CharField(max_length=20)
    login_pwd=models.CharField(max_length=20)
    log_for=models.ForeignKey(Customer)


    def __unicode__(self):
        return '%s' % self.login_name  
