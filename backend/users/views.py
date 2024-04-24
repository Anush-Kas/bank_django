from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import CustomUserCreateForm
from .models import CustomUser
from bank.models import Accountant, Client, Manager, Director


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.role == CustomUser.Roles.ACCOUNTANT:
                Accountant.objects.create(user=user)
            if user.role == CustomUser.Roles.CLIENT:
                Client.objects.create(user=user)
            if user.role == CustomUser.Roles.MANAGER:
                Manager.objects.create(user=user)
            if user.role == CustomUser.Roles.DIRECTOR:
                Director.objects.create(user=user)
            login(request, user)
            return redirect("bank:index")
    form = CustomUserCreateForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})