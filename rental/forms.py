from django import forms
from .models import Rental, Message, RentalItem
from parking.models import Listing
from multiselectfield import MultiSelectField
# from bootstrap_datepicker_plus import DatePickerInput


'''
Need:
    A. Booking Form for Rental Request
        1. Needs to Show listing
        2. Needs to Show Date/Times Requesting
        3. Needs to Show User Inputs for Vehicle Types
        4. Needs to Show a Total Estimate 
    B. Message Form:?? 
        1. Needs to show rental request status
        2. Needs to show listing
        3. To be viewed in an inbox

'''
vehicle_choices = ((1, 'Compact/Sedan'),
               (2, 'Truck/SUV'),
               (3, 'Van'),
               (4, 'Motocycle/Moped'),
               (5, 'Motorhome or Oversized'))



class RentalForm(forms.Form):
    """Form for Rental Request without Model"""

    vehicles = forms.CharField(label="What type of vehicle do you have?", widget = forms.Select(choices=vehicle_choices))

    comment = forms.CharField(label = 'Anything you want the renter to know?', widget=forms.Textarea)
    
    date = forms.DateField()
    time = forms.TimeField()

    duration = forms.IntegerField(label="How many hours will you need parking for? (One hour minimum)", max_value=24, min_value=1)
     
    ############ Calendar Attempts ##################
    
    # date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
    # calendar = forms.SplitDateTimeField(widget=forms.SplitDateTimeWidget)
    # calendar = forms.DateField(
    #     widget=DatePickerInput(format='%m/%d/%Y')
    # )

class MessageForm(forms.ModelForm):
    """Form for the Message model"""
    class Meta:
        model = Message
        fields = ('msg_content',)