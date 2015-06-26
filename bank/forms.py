from django import forms


OPEN_BALANCE_CHOICES=(
    (500,500),
    (1000,1000),
    (10000,10000),
)

ACCOUNT_TYPE=(
    ('savings','SAVINGS'),
    ('current','CURRENT'),
    ('fixed','FIXED'),
)

class CreateAccount(forms.Form):
    open_balance=forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=OPEN_BALANCE_CHOICES)
    acc_type=forms.MultipleChoiceField(required=True,widget=forms.CheckboxSelectMultiple,choices=ACCOUNT_TYPE)
    acc_pwd=
    acc_rpwd=
    balance=
    open_date=

 
    