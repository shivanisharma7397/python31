from django.shortcuts import render
from .forms import empform, clientform
from django.http import HttpResponse,HttpResponseRedirect
from .models import employee,client
# Create your views here.


def empviews(r):
    form = empform()
    if r.method == 'POST':
        form = empform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/carloan/empdata')
    return render(r,'tempapp/emp.html',{'form':form})

def empdatafetch(r):
    obj = employee.objects.all()
    return render(r,'tempapp/empdatafetch.html',{'obj':obj})

def clientviews(r):
    form = clientform()
    if r.method == 'POST':
        form = clientform(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
    return render(r,'tempapp/client.html',{'form':form})

def clientdatafetch(r):
    obj = client.objects.all()
    return render(r,'tempapp/clientdatafetch.html',{'obj':obj})