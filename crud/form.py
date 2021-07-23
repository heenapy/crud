from django import forms
from .models import Employee


class employeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['ename','email','password','contact']

