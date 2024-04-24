from django.contrib import admin

from .models import Bank, Accountant, Director, Manager, Client


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'min_client_deposit', 'director')


@admin.register(Accountant)
class AccountantAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bank', 'salary')


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bank')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
        list_display = ('id', 'user', 'bank', 'salary', 'accountant')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
        list_display = ('id', 'user', 'money', 'bank', 'manager')
