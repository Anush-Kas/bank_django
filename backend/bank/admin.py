from django.contrib import admin

from .models import Bank, Accountant, Manager, Client


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'min_client_deposit')


@admin.register(Accountant)
class AccountantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'bank', 'salary')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
        list_display = ('id', 'name', 'bank', 'salary', 'accountant')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
        list_display = ('id', 'name', 'money', 'bank', 'manager')