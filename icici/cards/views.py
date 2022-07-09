from django.shortcuts import render
from .forms import credit_form,fast_tag_form
from django.http import HttpResponseRedirect,HttpResponse
from .models import credit,fast_tag
# Create your views here.

def credit_views(r):
    form = credit_form()
    if r.method=='POST':
        form =  credit_form(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(r,'tempapp/cards/credit.html',{'form':form})

def credit_data(r):
    obj = credit.objects.all()
    return render(r,'tempapp/cards/creditdata.html',{'obj':obj})

def fast_tag_views(r):
    form = fast_tag_form()
    if r.method=='POST':
        form =  fast_tag_form(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(r,'tempapp/cards/fast_tag.html',{'form':form})

def fast_tag_data(r):
    obj = fast_tag.objects.all()
    return render(r,'tempapp/cards/fastagdata.html',{'obj':obj})