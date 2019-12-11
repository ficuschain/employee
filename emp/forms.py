from django import forms
from django.forms import ModelForm
from .models import Employee

class EmpForm(ModelForm):
    class Meta:
        model=Employee
        fields=['name','position','salary']