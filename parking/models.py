from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField
from django.db import models
import datetime
from django.urls import reverse
from django.core.exceptions import ValidationError

# third party
from django_google_maps import fields as map_fields

# Forced property for VS Code // Django adds dynamically
objects = models.Manager()


# Address Model
class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address1 = models.CharField(
        "Address line 1", max_length=1024, default=None, blank=True, null=True)
    address2 = models.CharField(
        "Address line 2", max_length=1024, default=None, blank=True, null=True)
    city = models.CharField("City", max_length=1024,
                            default=None, blank=True, null=True)
    state = models.CharField("State", max_length=1024,
                             default=None, blank=True, null=True)
    zip = models.CharField("ZIP/Postal Code", max_length=12,
                           default=None, blank=True, null=True)

    # Forced property for VS Code // Django adds dynamically
    objects = models.Manager()


    def __str__(self):
        return str(self.address_id)

    def instance(self):
        return Address

# Images Model
class Images(models.Model):
    images_id = models.AutoField(primary_key=True)
    image1 = models.ImageField(
        upload_to='listing_images/1/%Y/%m/%d/', blank=True)
    image2 = models.ImageField(
        upload_to='listing_images/2/%Y/%m/%d/', blank=True)
    image3 = models.ImageField(
        upload_to='listing_images/3/%Y/%m/%d/', blank=True)
    image4 = models.ImageField(
        upload_to='listing_images/4/%Y/%m/%d/', blank=True)

    # Forced property for VS Code // Django adds dynamically
    objects = models.Manager()

    def __str__(self):
        return str(self.images_id)

    def instance(self):
        return Images


# Model for a parking rental listing: Includes Vehicle and Parking class Enumerations
class Listing(models.Model):

    ################ Class ENUMS #######################
    # Model for types of vehicles
    class Vehicle(models.TextChoices):
        CAR = 'C', _('Compact/Sedan')
        TRUCK = 'T', _('Truck/SUV')
        VAN = 'V', _('Van')
        MOTOR = 'M', _('Motocycles/Moped')
        OVER = 'O', _('Motorhomes or Oversized')

        def __str__(self):
            return self.vehicle

    # Model for types of parking lots
    class Parking(models.TextChoices):
        RESIDENTIAL = 'R', _('Residential/Private')
        GARAGE = 'G', _('Garage')
        LOT = 'L', _('Parking Lot')
        STREET = 'S', _('Street Parking')
        OTHER = 'O', _('Other/Misc.')

        def __str__(self):
            return self.parking

    ############## DB Fields #############################
    listing_id = models.AutoField(primary_key=True)
    lister = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    hourly_Rate = models.DecimalField(decimal_places=2, max_digits=6)
    day_Rate = models.DecimalField(decimal_places=2, max_digits=6)
    overNight = models.BooleanField()
    parking_Pass = models.BooleanField()
    meet_Renter = models.BooleanField()

    vehicles = MultiSelectField(choices=Vehicle.choices, min_choices=1)

    parking = MultiSelectField(choices=Parking.choices, min_choices=1)

    # used for bookings
    is_Rented = models.BooleanField(default=False)

    # foriegn key links
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    images = models.ForeignKey(Images, on_delete=models.CASCADE)

    # Forced property for VS Code // Django adds dynamically
    objects = models.Manager()

    def __str__(self):
        return str(self.listing_id)

    def get_lister(self):
        return self.lister

    def instance(self):
        return Listing
