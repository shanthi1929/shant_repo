import datetime

from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect

from bank.models import Customer, Account, Transaction


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
        first_name=request.POST['post_fname'], 
        last_name=request.POST['post_lname'],
        address=request.POST['post_addr'],
        city=request.POST['city'],
        state=request.POST['state'],
        cust_mail=request.POST['email'],
        phone=request.POST['post_mob'],
        ssn=request.POST['post_ssn'],
        login_name=request.POST['post_username'],
        login_pwd=request.POST['post_rpwd'],
        )

    inx.save()
    
    #bank = get_object_or_404(Customer, pk=request.POST.get('cust_id'))
    return render(request, 'bank/reg_succes.html')
    

def login_page(request):
    return render(request, 'bank/login.html')

def login_check(request):
    l_user=request.POST['post_lid']
    l_pwd=request.POST['post_lpwd']

    print(l_user, l_pwd)
    
    u = Customer.objects.filter(login_name=l_user, login_pwd=l_pwd)

    if u:
        #print("Login Successfull")
        return render(request, 'bank/account_det.html')
    else:
        #print("Username and Password does not match...Try Again")
        return render(request, 'bank/login.html')



def account_page(request):  
    return render(request, 'bank/account_det.html')


def create_page(request):   
    return render(request, 'bank/acc_create.html')


def modify_page(request):   
    return render(request, 'bank/acc_modify.html')


def delete_page(request):   
    return render(request, 'bank/acc_delete.html')
