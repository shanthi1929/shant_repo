from django.db import models
from django.db.models import permalink



class Customer(models.Model):
	
	cust_id=models.IntegerField()
	first_Name=models.CharField(max_length=20)
	last_name=models.CharField(max_length=20)
	address=models.TextField(max_length=40)
	city=models.CharField(max_length=15)
	state=models.CharField(max_length=10)
	phone=models.IntegerField()
	ssn=models.IntegerField()
	join_date=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s' % self.first_Name

	# @permalink
	# def get_absolute_url(self):
	# 	return ('view_cust_details', None, { 'slug': self.slug })


class Transaction(models.Model):
	acc_num=models.IntegerField()
	amount=models.IntegerField()
	transdate=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return '%s' % self.acc_num

	# @permalink
	# def get_absolute_url(self):
	# 	return ('view_trans_details', None, { 'slug': self.slug })


class Account(models.Model):

    name = models.CharField(max_length=20)
    acc_num = models.IntegerField()
    balance = models.IntegerField()
    open_balance=models.IntegerField()
    cust_id=models.IntegerField()
    date_opened=models.DateTimeField(auto_now_add=True)
    interest=models.IntegerField()
    customer=models.ForeignKey(Customer)
    transaction=models.ForeignKey(Transaction)

    def __unicode__(self):
    	return '%s' % self.cust_id

    # @permalink
    # def get_absolute_url(self):
    # 	return ('view_account_details', None, { 'slug': self.slug })

# Create your models here.
