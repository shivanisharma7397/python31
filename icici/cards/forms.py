from django import forms
from .models import credit, fast_tag


class credit_form(forms.ModelForm):
    class Meta:
        model = credit
        fields = '__all__'


class fast_tag_form(forms.ModelForm):
    class Meta:
        model = fast_tag
        fields = '__all__'
