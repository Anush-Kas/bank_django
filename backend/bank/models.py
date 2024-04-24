from django.db import models

from users.models import CustomUser


class Bank(models.Model):
    name = models.CharField(verbose_name='Name of the bank', max_length=200)
    min_client_deposit = models.IntegerField(verbose_name='Min client deposit')
    director = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='banks')

    def __str__(self):
        return self.name


class Director(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='director')
    bank = models.ForeignKey(to=Bank, on_delete=models.CASCADE, related_name='directors', null=True, blank=True)


class Accountant(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='accountant')
    salary = models.IntegerField(verbose_name='Salary', default=0)
    bank = models.ForeignKey(to=Bank, on_delete=models.CASCADE, related_name='accountants', null=True, blank=True)


class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='manager')
    salary = models.IntegerField(verbose_name='Salary', default=0)
    accountant = models.ForeignKey(Accountant, verbose_name='Accountant of the manager',
                                   on_delete=models.CASCADE, related_name='managers')
    bank = models.ForeignKey(to=Bank, on_delete=models.CASCADE, related_name='managers', null=True, blank=True)


class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='client')
    money = models.IntegerField(verbose_name='Salary', default=0)
    manager = models.ForeignKey(Manager, verbose_name='Accountant of the manager',
                                on_delete=models.CASCADE, related_name='clients')
    bank = models.ForeignKey(to=Bank, on_delete=models.CASCADE, related_name='clients', null=True, blank=True)
