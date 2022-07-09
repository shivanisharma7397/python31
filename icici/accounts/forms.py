from django import forms
from .models import saving,current,fixed_deposit


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