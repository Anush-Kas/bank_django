from django.db import models

from users.models import CustomUser


class Bank(models.Model):
    name = models.CharField(verbose_name='Name of the bank', max_length=200)
    min_client_deposit = models.IntegerField(verbose_name='Min client deposit')
    director = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='banks')

    def __str__(self):
        return self.name


class BankUsers(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_banks')
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank_users')


class Accountant(models.Model):
    name = models.CharField(verbose_name='Name of the accountant', max_length=200)
    salary = models.IntegerField(verbose_name='Salary', default=0)
    bank = models.ForeignKey(
        Bank,
        verbose_name='Bank of the accountant',
        on_delete=models.CASCADE,
        related_name='accountants'
    )


class Manager(models.Model):
    name = models.CharField(verbose_name='Name of the manager', max_length=200)
    salary = models.IntegerField(verbose_name='Salary', default=200)
    bank = models.ForeignKey(Bank, verbose_name='Bank of the manager',
                             on_delete=models.CASCADE, related_name='manager')
    accountant = models.ForeignKey(Accountant, verbose_name='Accountant of the manager',
                                   on_delete=models.CASCADE, related_name='managers')


class Client(models.Model):
        name = models.CharField(verbose_name="Name of the client", max_length=200)
        money = models.IntegerField(verbose_name='Money', default=10000)
        manager = models.ForeignKey(Manager, verbose_name='Manager of the client',
                                    on_delete=models.CASCADE, related_name='clients')
        bank = models.ForeignKey(Bank, verbose_name='Bank of the client',
                                 on_delete=models.CASCADE, related_name='clients')