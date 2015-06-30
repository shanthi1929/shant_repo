from django import forms
from .models import Account

TITLE_CHOICES = (
    ('SAVINGS', 'savings'),
    ('CURRENT', 'current'),
    ('FIXED', 'fixed'),
)

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = (
            'acc_num', 'acc_type', 'acc_pwd','acc_pwd_one',
                )
        widgets = {
            'acc_num': forms.TextInput
            (
                attrs={
                    'placeholder':'Enter Account Number',
                    'class':'col-md-12 form-control'
                }
            ),
            'acc_type': forms.TextInput
            (
                attrs={
                    'placeholder':'Enter a Account Type',
                    'class':'form-control'
                }
            ),
            'acc_pwd': forms.PasswordInput
            (
               
            ),
             'acc_pwd_one': forms.PasswordInput
            (
                # attr={
                #     'placeholder':'Repeat Password',
                #     'class':'col-md-12 form-control'
                # }

            ),

        }

    