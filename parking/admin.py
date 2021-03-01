from django.contrib import admin


from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

# Register your models here.
from .models import Address, Images, Listing



class RentalAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }

admin.site.register(Address, RentalAdmin)
admin.site.register(Images)
admin.site.register(Listing)
