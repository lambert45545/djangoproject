from django import forms
from .models import  Lawyer,Cases,Client

class ClientForm(forms.ModelForm):
    class Meta :
        model=Client
        fields=["first_name","last_name","email","phone","gender"]


class LawerForm(forms.ModelForm):
    class Meta:
        model=Lawyer
        fields=["first_name","last_name","email","phone"]

class CasesForm(forms.ModelForm):
    class Meta :
        model = Cases
        fields=["title","description","statue","lawyer","client"]
