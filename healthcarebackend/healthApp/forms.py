from django import forms

# from healthcarebackend.healthApp.models import Patient
from healthApp.models import Patient


class PatientLoginForm(forms.Form):

    phoneNo = forms.CharField()
    password = forms.CharField()


class PatientRegisterForm(forms.ModelForm):

    model = Patient
    include = ["*"]