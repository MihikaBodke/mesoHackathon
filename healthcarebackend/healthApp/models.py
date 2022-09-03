from pydoc import pathdirs
from django.db import models
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.

class Patient(models.Model):

    name = models.CharField(max_length=50)
    phoneNo = models.IntegerField()
    mail = models.EmailField()
    password = models.CharField(max_length=20)

class Doctor(models.Model):
    first_name = models.CharField(max_length = 25)
    last_name = models.CharField(max_length = 25)
    specialization = models.CharField(max_length = 30)
    degree = models.CharField(max_length = 10)
    age = models.IntegerField()
    years_of_experience = models.IntegerField()
    contact_no = models.IntegerField()
    email = models.CharField(max_length = 55)

class Hospital(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 255)
    city = models.CharField(max_length = 30)
    state = models.CharField(max_length = 30)
    pincode = models.IntegerField()
    no_of_beds = models.IntegerField()
    no_of_doctors = models.IntegerField()
    email = models.CharField(max_length=35)
    contact_no = models.IntegerField()

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey( Doctor, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    location = models.CharField(max_length=100)
    mode = models.CharField(max_length=20) #virtual or inperson
    amount = models.CharField(max_length=10)


class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.CharField(max_length=50, default='', blank=True)

    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    pname = models.CharField(max_length=50, default='', blank=True)
    dname = models.CharField(max_length=50, default='', blank=True)
    labtime = (
        ('08:00 – 09:00', '08:00 – 09:00'),
        ('09:00 – 10:00', '09:00 – 10:00'),
        ('10:00 – 11:00', '10:00 – 11:00'),
        ('11:00 – 12:00', '11:00 – 12:00'),
        ('12:00 – 13:00', '12:00 – 13:00'),
        ('13:00 – 14:00', '13:00 – 14:00'),
        ('14:00 – 15:00', '14:00 – 15:00'),
        ('15:00 – 16:00', '15:00 – 16:00'),
        ('16:00 – 17:00', '16:00 – 17:00'),
        ('17:00 – 18:00', '17:00 – 18:00'),
    )
    labtime = models.CharField(max_length=25, choices=labtime, default="labtime")
    date = models.DateField(default=datetime.datetime.today)

    def placeOrder(self):
        self.save()

class PlaceOrder(models.Model):
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")