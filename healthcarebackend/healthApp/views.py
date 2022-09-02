from django.shortcuts import render
from django.http import HttpResponse
from .forms import PatientLoginForm
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