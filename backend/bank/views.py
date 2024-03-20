from django.shortcuts import render, redirect
from .models import Bank, Accountant, BankUsers
from .forms import BankForm, AccountantForm
from django.contrib.auth.decorators import login_required
from users.models import CustomUser


# CBV - class based views
# FBV - function based views

# @login_required
# def banks(request):
#     banks = Bank.objects.all()
#     return render(request, "bank/banks.html", context={'banks': banks})
#
#
# @login_required
# def create_bank(request):
#     form = BankForm()
#     if request.method == 'GET':
#         return render(request, "bank/create_bank.html", context={'form': form})
#     elif request.method == 'POST':
#         form = BankForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('bank:banks')
#     return render(request, "bank/create_bank.html", context={'form': form})
#
#
# @login_required
# def accountant(request):
#     accounts = Accountant.objects.all()
#     return render(request, "bank/accounts.html", context={'account': accounts})
#
#
# @login_required
# def create_accountant(request):
#     form = AccountantForm()
#     if request.method == 'GET':
#         return render(request, "bank/create_accountant.html", context={'form': form})
#     elif request.method == 'POST':
#         form = AccountantForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('bank:accounts')
#     return render(request, "bank/create_accountant.html", context={'form': form})
# Create Manager


# director
@login_required
def create_bank(request):
    if request.user.role != CustomUser.Roles.DIRECTOR:
        return redirect('login')
    form = BankForm()
    if request.method == 'GET':
        return render(request, "bank/create_bank.html", context={'form': form})
    elif request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            bank = form.save(commit=False)
            bank.director = request.user
            bank.save()
            return redirect('bank:bank_info', bank.id)
    return render(request, "bank/create_bank.html", context={'form': form})


# accountant and director
def managers():
    pass


# director accountant manager
def clients(request):
    pass


# all
def bank_info(request, bank_id):
    bank = Bank.objects.get(pk=bank_id)
    print(request.user)
    print(bank.director)
    if request.user == bank.director:
        return render(request, "bank/bank.html", context={'bank': bank})
    relation = BankUsers.objects.filter(user=request.user, bank=bank)
    if relation:
        return render(request, "bank/bank.html", context={'bank': bank})
    return redirect('bank:index')



# all
def profile(request):
    pass



def index(request):
    return render(request, "bank/index.html")