from django import forms
from django.forms.widgets import ClearableFileInput
from django.contrib import admin
from .models import Images, Listing, Address

# Layout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class ListingForm(forms.ModelForm):
    """Form for the Listing model"""
    class Meta:
        model = Listing
        fields = ('title', 'description', 'hourly_Rate', 'day_Rate', 'overNight', 'parking_Pass', 'meet_Renter', 'vehicles', 'parking', 'date', 'time',)
        exlude = ('address', 'images',)


class AddressForm(forms.ModelForm):
    """Form for the Address model"""
    class Meta:
        model = Address
        fields = ('address1', 'address2', 'city', 'state', 'zip',)

# class AddressAdmin(admin.ModelAdmin):
#     class form(forms.ModelForm):
#         class Meta:
#             widgets = {
#                 'address': AddressWithMapWidget({'class': 'vTextField'})
#             }

    #Needs to call the http geocoding address


class ImageForm(forms.ModelForm):
    """Form for the Image model"""
    class Meta:
        model = Images
        fields = ('image1', 'image2', 'image3', 'image4')

