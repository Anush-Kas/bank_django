from django import forms
from bank.models import Bank
from bank.models import Manager, Client, Accountant
#
#
class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ('name', 'min_client_deposit')
#
#
# class AccountantForm(forms.ModelForm):
#     class Meta:
#         model = Accountant
#         fields = ('name', 'bank', 'salary')
#
#


class AccountantForm(forms.Form):
    accountant = forms.ModelChoiceField(queryset=Accountant.objects.all(), label='Accountant')
    salary = forms.IntegerField(min_value=100, label='Salary')


class ManagerForm(forms.Form):
    manager = forms.ModelChoiceField(queryset=Manager.objects.all(), label='Manager')
    accountant = forms.ModelChoiceField(queryset=Accountant.objects.all(), label='His Accountant')
    salary = forms.IntegerField(min_value=100, label='Salary')


class ClientsForm(forms.ModelForm):
    manager = forms.ModelChoiceField(queryset=Manager.objects.all(), label='His Manager')
    client = forms.ModelChoiceField(queryset=Client.objects.all(), label='Client')
    money = forms.IntegerField(min_value=100, label='Deposit')


