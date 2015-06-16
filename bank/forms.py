# from django import forms
# import re
# from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist


# class RegistrationForm(forms.Form):
# 	c_id=forms.IntegerField(label='Customer id:')
# 	f_name=forms.CharField(label='First Name:', max_length=20)
# 	l_name=forms.CharField(label='Last Name:', max_length=20)
# 	addr=forms.CharField(label='Address:')
# 	cit=forms.CharField(label='City:', max_length=20)
# 	stat=forms.CharField(label='State:', max_length=20)
# 	ph=forms.IntegerField(label='Mobile Number:')
# 	sn=forms.CharField(label='SSN:', max_length=20)
# 	j_date=forms.DateTimeField(label='Joining Date:')
# 	passwd1=forms.CharField(label='Create Password:',widget=forms.PasswordInput())
# 	passwd2=forms.CharField(label='Re-Enter Password',widget=forms.PasswordInput()
# 	)

# def clean_pwd2(self):
# 	if 'passwd1' in self.clean_data:
# 		passwd1=self.clean_data['passwd1']
# 		passwd2=self.clean_data['passwd2']
# 		if passwd1==passwd2:
# 			return passwd2
# 	raise forms.ValidationError('Passwords do not match')

# def clean_name(self):
# 	f_name=self.clean_data['f_name']
# 	l_name=self.clean_data['l_name']

# 	if not re.search(r'^\w+$',f_name,l_name):
# 		raise forms.ValidationError('Username can contain alphanumeric characters and underscore only')
# 	else:
# 		return f_name,l_name
