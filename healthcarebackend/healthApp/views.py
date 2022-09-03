from .forms import ScheduleAppointmentForm
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PatientLoginForm
from django.views import View
from django.contrib import messages
from .models import Hospital, Patient, Doctor, Appointment, Product, Category, Order
from django.views.decorators.csrf import csrf_exempt

MERCHANT_KEY = "i4_MxwJOYZ@o4dxe"

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

def appointmentList(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'patient/appointment_list.html', {'appointments': appointments})


def lab1(request):
    return render(request, 'lab_test.html')

class lab2(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect('lab2')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None

        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()

        data = {}
        data['products'] = products
        data['categories'] = categories

        return render(request, 'lab2.html', data)


class CheckOut1(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.POST.get('pname')
        amount = request.POST.get('amount')
        quantity = request.POST.get('quantity')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        for product in products:
            order = Order(customer=customer,
                          product=product,
                          price=amount,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            id = order.id
        request.session['cart'] = {}
        param_dict = {

            'MID': 'nVKXUm57274101057469',
            'ORDER_ID': str(order.id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'shop/paytm.html', {'param_dict': param_dict})

@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        return render(request, 'cart.html', {'products': products})

class OrderView(View):
    def get(self, request):
        orders = Order.objects.filter(customer=request.user)
        return render(request, 'orders.html', {'orders': orders})