from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import Customer, Loan_app
from django.forms import fields
from django.core.exceptions import ValidationError


def validate_pos(value):
    if value <= 0:
        raise ValidationError(
            (f'{value} is not a valid value'),
            params={'value': value},
        )


class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=15)
    last_name = forms.CharField(max_length=15)
    company_name = forms.CharField(max_length=15)
    salary = forms.IntegerField(validators=[validate_pos])

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'company_name', 'salary']


class LoanAppForm(forms.Form):
    amount = forms.IntegerField(validators=[validate_pos])

    class Meta:
        model = Loan_app
        fields = ['amount']
