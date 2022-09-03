from django.contrib import admin

from healthApp.models import Appointment, Hospital, Patient, Doctor

# Register your models here.
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(Appointment)
admin.site.register(Doctor)

