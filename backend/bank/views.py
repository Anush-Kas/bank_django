from django.shortcuts import render, redirect
from bank.models import Bank, Accountant, Director, Client, Manager
from .forms import BankForm, AccountantForm, ManagerForm, ClientsForm
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from random import choice


# CBV - class based views
# FBV - function based views

# @login_required
# def banks(request):
#     banks = Bank.objects.all()
#     return render(request, "bank/banks.html", context={'banks': banks})
#
#
# @login_required
# def accountant(request):
#     accounts = Accountant.objects.all()
#     return render(request, "bank/accounts.html", context={'account': accounts})
#
#
@login_required
def create_accountant(request):
    if request.user.role != CustomUser.Roles.DIRECTOR:
        return redirect('bank:index')
    form = AccountantForm()
    if request.method == 'GET':
        return render(request, "bank/create_accountant.html", context={'form': form})
    elif request.method == 'POST':
        form = AccountantForm(request.POST)
        if form.is_valid():
            accountant = form.cleaned_data['accountant']
            accountant.salary = form.cleaned_data['salary']
            accountant.bank = request.user.director.bank
            accountant.save()
            return redirect('bank:index')
    return render(request, "bank/create_accountant.html", context={'form': form})
# Create Manager


# director
@login_required
def create_bank(request):
    if request.user.role != CustomUser.Roles.DIRECTOR:
        return redirect('bank:index')
    form = BankForm()
    if request.method == 'GET':
        return render(request, "bank/create_bank.html", context={'form': form})
    elif request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            director = request.user.director
            bank.director = director
            director.bank = bank
            bank.save()
            return redirect('bank:bank_info', bank.id)
    return render(request, "bank/create_bank.html", context={'form': form})



# Check
# accountant and director
def create_manager(request):
    if request.user.role != CustomUser.Roles.DIRECTOR:
        return redirect('login')
    form = ManagerForm()
    if request.method == 'GET':
        return render(request, "bank/create_manager.html", context={'form': form})
    elif request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank:manager')
    return render(request, "bank/create_manager.html", context={'form': form})



# Check
# director accountant manager
def create_client(request):
    if request.user.role != CustomUser.Roles.DIRECTOR:
        return redirect('login')
    form = ClientsForm()
    if request.method == 'GET':
        return render(request, "bank/create_client.html", context={'form': form})
    elif request.method == 'POST':
        form = ClientsForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.bank = request.user.bank
            if client.money < client.bank.min_client_deposit:
                return render(request, "bank/create_client.html", context={'form': form})
            else:
                client.manager = choice(client.bank.managers.all())
                client.save()
                return redirect("bank:bank_info", client.bank.id)


# all
def bank_info(request, bank_id):
    bank = Bank.objects.get(pk=bank_id)
    if Director.objects.filter(user=request.user, bank=bank).exists():
        return render(request, "bank/bank.html", context={'bank': bank})
    if Manager.objects.filter(user=request.user, bank=bank).exists():
        return render(request, "bank/bank.html", context={'bank': bank})
    if Accountant.objects.filter(user=request.user, bank=bank).exists():
        return render(request, "bank/bank.html", context={'bank': bank})
    if Client.objects.filter(user=request.user, bank=bank).exists():
        return render(request, "bank/bank.html", context={'bank': bank})
    return redirect('bank:index')



# all
def profile(request):
    pass



def index(request):
    return render(request, "bank/index.html")