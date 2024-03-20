from django import forms

from .models import Bank, Accountant


class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ('name', 'min_client_deposit')


class AccountantForm(forms.ModelForm):
    class Meta:
        model = Accountant
        fields = ('name', 'bank', 'salary')
