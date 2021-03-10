from django.contrib import admin

# Register your models here.
from .models import RentalItem, Rental, Message, LovedRentals

admin.site.register(RentalItem)
admin.site.register(Rental)
admin.site.register(Message)
admin.site.register(LovedRentals)