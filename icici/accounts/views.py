from django.shortcuts import render
from .forms import saving_form, current_form, fixed_deposit_form, signupform
from django.http import HttpResponseRedirect, HttpResponse
from .models import saving, current, fixed_deposit
from django.contrib.auth.decorators import login_required


# Create your views here.


def saving_views(r):
    form = saving_form()
    if r.method == 'POST':
        form = saving_form(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(r, 'tempapp/accounts/saving.html', {'form': form})


@login_required
def saving_data(r):
    obj = saving.objects.all()
    return render(r, 'tempapp/accounts/savingdata.html', {'obj': obj})


def current_views(r):
    form = current_form()
    if r.method == 'POST':
        form = current_form(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(r, 'tempapp/accounts/current.html', {'form': form})


@login_required
def current_data(r):
    obj = current.objects.all()
    return render(r, 'tempapp/accounts/currentdata.html', {'obj': obj})


def fixed_deposit_views(r):
    form = fixed_deposit_form()
    if r.method == 'POST':
        form = fixed_deposit_form(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(r, 'tempapp/accounts/fixed_deposit.html', {'form': form})


@login_required
def fixed_deposit_data(r):
    obj = fixed_deposit.objects.all()
    return render(r, 'tempapp/accounts/fixed_deposit_data.html', {'obj': obj})


def logout(r):
    return render(r, "tempapp/logout.html")


def signup(r):
    form = signupform()
    if r.method == 'POST':
        form = signupform(r.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
        return render(r, 'tempapp/signup.html', {'form': form})
