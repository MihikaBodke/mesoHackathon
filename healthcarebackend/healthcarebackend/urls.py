"""healthcarebackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('bog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from healthApp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name = "index"),
    # path('send/', send_notification),
    path('getAppointments', getAppointments, name = 'getappointment'),
    path("scheduleAppointment/", scheduleAppointment, name = 'bookappointment'),
    path('',include('face_app.urls')),
    path('lab1/', lab1, name='lab1'),
    path('lab2/', lab2.as_view(), name='lab2'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', CheckOut1.as_view(), name='checkout'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('handle_request/', handlerequest, name='handlerequest'),
    path('home/', landing, name='home'),
    path('aboutus/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('profile/', profile, name='profile'),
    path('doctor/', doctor, name='doctor'),
    path('face_mask/', include('face_app.urls'), name = 'face_detection'),
    path('login/', login, name='login'),
    path("verified/", verified, name="verified",)

] + staticfiles_urlpatterns()

# static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)