import datetime

from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

from bank.models import Customer, Account, Transaction, Login_details
from bank.forms import *


#def index(request):
 #   return HttpResponse('Hello World!!!!')


#def current_datetime(request):
 #   now = datetime.datetime.now()
  #  html = "<html><body>It is now %s.</body></html>" % now
   # return HttpResponse(html)

#def base(request):
 #   return render(request, 'bank/test.html')


#def search(request):
 #   if 'q' in request.GET:
  #      message = 'You searched for: %r' % request.GET['q']
   # else:
    #    message = 'You submitted an empty form.'
    #return HttpResponse(message)
def main_page(request):
    template=get_template('bank/main_page.html')
    variables=Context({
        'head_title':'Banking Application',
        'page_title':'Welcome to Jango Bank',
        'page_body':'Every Day Of Our Lives We Make Deposits In The Memory Banks Of Our Children'
        })
    output=template.render(variables)
    return HttpResponse(output)


def register_page(request):
    return render(request, 'bank/register.html')


def register_check(request):

    inx = Customer(
        # cust_id=request.POST['post_identify'],
        first_Name=request.POST['post_fname'], 
        last_name=request.POST['post_lname'],
        address=request.POST['post_addr'],
        city=request.POST['city'],
        state=request.POST['state'],
        cust_mail=request.POST['email'],
        # phone=request.POST['post_mob'],
        phone=9987,
        # ssn=request.POST['post_ssn'],
        ssn=3306, )

    inx.save()

    bank = get_object_or_404(Customer, pk=request.POST.get('cust_id'))
    return render(request, 'bank/login.html', {'bank': bank})
    

def login_page(request):
    #template=get_template('bank/register.html')
    return render(request, 'bank/login.html')


def account_page(request):  
    return render(request, 'bank/account_det.html')


def create_page(request):   
    return render(request, 'bank/acc_create.html')


def modify_page(request):   
    return render(request, 'bank/acc_modify.html')


def delete_page(request):   
    return render(request, 'bank/acc_delete.html')
