from django import forms
from .models import Rental, Message, RentalItem
from parking.models import Listing
from multiselectfield import MultiSelectField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, HTML, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


vehicle_choices = ((1, 'Compact/Sedan'),
                   (2, 'Truck/SUV'),
                   (3, 'Van'),
                   (4, 'Motocycle/Moped'),
                   (5, 'Motorhome or Oversized'))



class RentalForm(forms.Form):
    """Form for Rental Request without Model"""

    vehicles = forms.CharField(
        label="What type of vehicle do you have?", widget=forms.Select(choices=vehicle_choices))

    comment = forms.CharField(
        label='Anything you want the renter to know?', widget=forms.Textarea)

    date = forms.DateField()
    time = forms.TimeField()

    duration = forms.IntegerField(
        label="How many hours will you need parking for? (One hour minimum)", max_value=24, min_value=1)

    # Styling addition
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                'Hi, {{ user.username }}!',
                Div(
                    'vehicles',
                    PrependedText('duration', 'hr/s'),
                    css_id='grid1Rental'
                ),
                Div(
                    Div(
                        HTML("""
                        <p><strong>When you need your spot?</strong></p>
                        """),
                        PrependedText(
                            'date', 'M/D/Y', placeholder="01/01/21", css_id='dateRental'),
                        PrependedText('time', 'Hr:Min',
                                      placeholder="05:00", css_id='timeRental'),
                        css_id='grid2Rental'
                    ),
                    'comment',
                    css_id="grid3Rental"
                ),
                Div(
                    FormActions(Submit('rent', 'Rent'))
                )
            )
        )


class MessageForm(forms.ModelForm):
    """Form for the Message model"""
    class Meta:
        model = Message
        fields = ('msg_content',)
