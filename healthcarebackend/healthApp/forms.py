from django import forms

# from healthcarebackend.healthApp.models import Patient
from healthApp.models import Patient
from healthApp.models import Appointment


class PatientLoginForm(forms.Form):

    phoneNo = forms.CharField()
    password = forms.CharField()


class PatientRegisterForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"
   
class ScheduleAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"