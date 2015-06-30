from django.db import models
from django.db import IntegrityError
from datetime import datetime
from django.forms import ModelForm

TITLE_CHOICES = (
    ('SAVINGS', 'savings'),
    ('CURRENT', 'current'),
    ('FIXED', 'fixed'),
)



# def get_today():
#     return datetime.date.today() 


class Customer(models.Model):

    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    address = models.TextField(max_length=40, null=True)
    cust_mail = models.EmailField(max_length=40, null=True)
    city = models.CharField(max_length=15, null=True)
    state = models.CharField(max_length=10, null=True)
    phone = models.BigIntegerField(default=0, null=True)
    ssn = models.IntegerField(default=0, null=True)
    join_date = models.DateTimeField(default=datetime.now(),editable=False)
    login_name = models.CharField(max_length=20, unique=True)
    login_pwd = models.CharField(max_length=20)

    # def __unicode__(self):
    #     return '%s' % self.login_name

    def __str__(self):
        return "{0} - {1} - {2}".format(
                self.first_name,
                self.login_name,
                self.ssn)


class Account(models.Model):

    acc_num = models.AutoField(primary_key=True)
    balance = models.IntegerField()
    open_balance = models.IntegerField(default=500)
    date_opened = models.DateTimeField(default=datetime.now(),editable=False)
    acc_type = models.CharField(null=True, max_length=20,choices=TITLE_CHOICES)
    acc_pwd = models.CharField(max_length=20)
    acc_pwd_one = models.CharField(max_length=20)
    cust_for = models.ManyToManyField(Customer)

    # def __unicode__(self):
    #     return '%s' % self.acc_num

    def __str__(self):
        return "{0} - {1}".format(
                self.acc_num,
                self.balance)


class Transaction(models.Model):

    acc_number=models.IntegerField()
    amount = models.IntegerField()
    cur_bal = models.IntegerField()
    trans_date = models.DateTimeField(auto_now_add=True)
    acc_for = models.ManyToManyField(Account)

    # def __unicode__(self):
    #     return '%s' % self.amount

    def __str__(self):
        return "{0} - {1}".format(self.amount, self.trans_date)



class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['acc_num','acc_type','acc_pwd','acc_pwd_one']

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['acc_number','amount','cur_bal']
