from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(validators=[MaxValueValidator(10)])
    booking_date = models.DateField(auto_now=False, auto_now_add=False)
    
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[MaxValueValidator(5)])