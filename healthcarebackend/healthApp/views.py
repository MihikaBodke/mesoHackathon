from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientLoginForm
from .models import Appointment, Patient
from .forms import ScheduleAppointmentForm
# Create your views here.



def index(request):
    return HttpResponse("<h1>Hello World!</h1>")

def patientLogin(request):
    if request.method == "POST":
        form = PatientLoginForm()
        
        if(form.is_valid()):

            return render(request, "")
    else:
        form = PatientLoginForm()
        return render(request, "", {"form":form})

def getAppointments(request, phoneNo):
    patient = Patient.objects.get(phoneNo = phoneNo)
    appointments = Appointment.objects.get(patient = patient)
    return HttpResponse(appointments)


def getAppointmentDetails(request, appointment):
    return Appointment.objects.get(id = appointment.id)

def scheduleAppointment(request):
    if request.method == "POST":
        form = ScheduleAppointmentForm()
    else:
        form = ScheduleAppointmentForm()
        return render(request, "ScheduleAppointmentForm.html", {"form":form})