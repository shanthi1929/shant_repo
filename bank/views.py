from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from bank.forms import *

import datetime



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
	#template=get_template('bank/register.html')
	return render(request, 'bank/register.html')

	# if request.method=='GET':
	# 	form=RegistrationForm(request.GET)
	# 	if form.is_valid():
	# 		user=User.objects.create_user(
	# 			f_name=form.clean_data['f_name'],
	# 			l_name=form.clean_data['l_name'],
	# 			passwd1=form.clean_data['passwd1'],
	# 			passwd2=form.clean_data['passwd2'],
	# 			addr=form.clean_data['addr'],
	# 			cit=form.clean_data['cit'],
	# 			stat=form.clean_data['stat'],
	# 			ph=form.clean_data['ph'],
	# 			ssn=form.clean_data['ssn'],
	# 			j_date=form.clean_data['j_date']

	# 			)
	# 		return HttpResponseRedirect('/')
	# 	else:
	# 		form=RegistrationForm()
	# 		variables=RequestContext(request,{
	# 			'form':form
	# 			})
	# 		return render_to_response(
	# 			'bank/register.html',variables
	# 			)

# Create your views here.
