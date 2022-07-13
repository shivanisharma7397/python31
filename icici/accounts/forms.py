from django import forms
from .models import saving,current,fixed_deposit
from django.contrib.auth.models import User

class saving_form(forms.ModelForm):
    class Meta:
        model = saving
        fields = '__all__'


class current_form(forms.ModelForm):
    class Meta:
        model = current
        fields = '__all__'

class fixed_deposit_form(forms.ModelForm):
    class Meta:
        model = fixed_deposit
        fields = '__all__'

class signupform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name','email']
        widgets = {'password':forms.PasswordInput()}     # to make password encrpyted at the front end