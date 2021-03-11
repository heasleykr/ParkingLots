from django import forms
from django.forms.widgets import ClearableFileInput
from django.contrib import admin
from .models import Images, Listing, Address

# Layout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, HTML, Submit
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions, PrependedAppendedText


class ListingForm(forms.ModelForm):
    """Form for the Listing model"""
    class Meta:
        model = Listing
        fields = ('title', 'description', 'hourly_Rate', 'day_Rate', 'overNight',
                  'parking_Pass', 'meet_Renter', 'vehicles', 'parking', 'date', 'time',)
        exlude = ('address', 'images',)

    # Styling addition
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div(
                    Div(
                        PrependedText('title', '<b>Listing Title: </b>'),
                        css_id='titleUpload'
                    ),
                    Div(
                        Div('vehicles', css_id='p_v_left'),
                        Div(
                            HTML("""
                            <p><i class="fas fa-chevron-left"></i>
                            What vehicles can your spot fit?</p>
                            <p> What type of spot is it?<i class="fas fa-chevron-right"></i></p>
                            """),
                            css_id='p_v_middle'
                        ),
                        Div('parking', css_id='p_v_right'),
                        css_id='listingUpload2'
                    ),
                    Div(
                        Div(
                            HTML("""
                            <h2>Your Listing Rates</h2>
                            <i class="fas fa-dollar-sign"></i>
                            """),
                            css_id='rateSide'
                        ),
                        Div(
                            PrependedAppendedText('hourly_Rate', '$', '.00'),
                            PrependedAppendedText('day_Rate', '$', '.00'),
                            css_id='rateInput'),
                        css_id='listingUpload3'
                    ),
                    Div(
                        Div(
                            HTML("""
                            <h2>Customize</h2>
                            """),
                            css_id='peopleIcon'
                        ),
                        Div(
                            HTML("""
                            <p>Is parking overnight allowed?</p>
                            """),
                            'overNight',
                            css_class='radioOptions'
                        ),
                        Div(
                            HTML("""
                            <p>Will you meed to meet renters?</p>
                            """),
                            'meet_Renter',
                            css_class='radioOptions'
                        ),
                        Div(
                            HTML("""
                            <p>Do they need a parking pass?</p>
                            """),
                            'parking_Pass',
                            css_class='radioOptions'
                        ),
                        css_id="listingUpload4"
                    ),
                    Div(
                        Div(
                            HTML("""
                            <h2>Describe your listing for renters</h2>
                            <i class="far fa-laugh-beam"></i>
                            """),
                            css_id='descripSide'
                        ),
                        'description',
                        css_id='listingUpload5'
                    ),
                    Div(
                        FormActions(Submit(
                            'Preview Listing', 'Preview Listing')),
                        css_id='btnListing'
                    ),
                    Div(
                        'date',
                        'time',
                        css_id='deleteMe'
                    ),
                    css_id="listingUploadDiv"
                )
            )
        )


class AddressForm(forms.ModelForm):
    """Form for the Address model"""
    class Meta:
        model = Address
        fields = ('address1', 'address2', 'city', 'state', 'zip',)

    # Styling addition
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.use_custom_control = True
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div(
                    Div(
                        PrependedText('address1', '<b>Street Name</b>'),
                        PrependedText('address2', '<b>Street Name</b>'),
                        PrependedText('city', '<b>City</b>'),
                        PrependedText('state', '<b>State</b>'),
                        PrependedText('zip', '<b>Zip/Postal</b>'),
                        css_id='addressDiv1'
                    ),
                    Div(
                        HTML("""
                        <h2>Parking Address</h2>
                        <i class="fas fa-map-marked-alt"></i>
                        """),
                        css_id='addressDiv2'
                    ),
                    css_id="addressDivMain"
                )
            )
        )


class ImageForm(forms.ModelForm):
    """Form for the Image model"""
    class Meta:
        model = Images
        fields = ('image1', 'image2', 'image3', 'image4')

    # Styling addition
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.use_custom_control = True
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Fieldset(
                'You can upload up to four: ',
                Div(
                    Div(
                        'image1',
                        'image2',
                        css_id='upload1'
                    ),
                    Div(
                        'image3',
                        'image4',
                        css_id='upload2'
                    ),
                    Div(
                        FormActions(Submit(
                            'Add Listing Details', 'Add Listing Details')),
                        css_id='btnImg'
                    ),
                    css_id="imgDiv2"
                )
            )
        )
