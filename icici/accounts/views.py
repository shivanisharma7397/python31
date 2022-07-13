from django.core.mail import send_mail
from django.shortcuts import render
from pyexpat.errors import messages

from .forms import saving_form, current_form, fixed_deposit_form, signupform
from django.http import HttpResponseRedirect, HttpResponse
from .models import saving, current, fixed_deposit
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.hashers import make_password, check_password

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
        encryptedpassword = make_password(r.POST['password'])
        print(encryptedpassword)
        form = signupform(r.POST)
        if form.is_valid():

            user = form.save()
            user.set_password(user.password)       #it will encrypt password in the database
            user.save()                            #password override with encrypted password

            return HttpResponseRedirect('/accounts/login')
    return render(r, 'tempapp/signup.html', {'form': form})


def send_gmail(request):
    if request.method=="POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, subject, message)

        send_mail(
            subject,
            message,
            'ajaypateldjango31@gmail.com',
            ['shivanisharma7397@gmail.com'],
            fail_silently=False,
        )

        return HttpResponseRedirect(reverse('/'))
    else:
        return HttpResponse('Invalid request')