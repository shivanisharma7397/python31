from django import forms
from .models import employee, client


class empform(forms.ModelForm):
    class Meta:
        model = employee
        fields = ['name','city','mobile']


class clientform(forms.ModelForm):
    class Meta :
        model = client
        fields = '__all__'