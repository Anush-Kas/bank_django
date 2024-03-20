from django.shortcuts import render, redirect
from django.contrib.auth import login

from .forms import CustomUserCreateForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("bank:index")
    form = CustomUserCreateForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})