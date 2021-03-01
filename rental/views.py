from django.shortcuts import render, redirect
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, CreateView
import json
from django.core import serializers
from .forms import RentalForm
from .models import Rental, RentalItem, Message

# Intra Module imports
from parking.models import Listing, Address, Images


#Search view that plots address on Google Maps
#Needs to call the http geocoding address
#def search():
    # http://maps.googleapis.com/maps/api/geocode/json?address=<address retrieved from form>&sensor=true

#Display all Listings from Database
def send_Listings(request): 

    #query DB and grab table data
    listings = Listing.objects.all().values()

    #variable declaration 
    listing_Dictionary = {} #list to be packaged
    i = 0 #increment element

    for list in listings: #loop through listings

        #Update Demical/Date/Time Objects for Serialization
        list['day_Rate'] = str(list['day_Rate'])
        list['hourly_Rate'] = str(list['hourly_Rate'])
        list['date'] = str(list['date'])
        list['time'] = str(list['time'])

        #TODO: grab correct data in Address/Images
        # address = list.address
        # images = list.images

        #Add to dictionary 
        listing_Dictionary[i] = list

        # increment counter
        i += 1

    # Serialize data 
    dataJSON = json.dumps(listing_Dictionary, indent = 4)

    #Write/Rewrite JSON to file
    with open("static/all_listings.txt", "w") as outfile:
        outfile.write(dataJSON)

    # render & send to listings.js
    return render(request, 'listings.html') 


#renders single listing with details
def single_Listing(request, listing_id):

    id = listing_id

    if request.method == "GET":
        #grad reguested listing by id
        theOne = Listing.objects.get(pk=id)

        print(theOne)

        #send to listing_single.html
    return render(request,'rentals/listing_single.html', {'listing': theOne})


#Rental Request Form / Creation
def rent_Listing(request, listing_id):

    id = listing_id
    #Grab listing from DB
    theOne = Listing.objects.get(pk=id)

    if request.method == "POST":
        #Grab Form entries
        posted_Form = RentalForm(request.POST)

        if posted_Form.is_valid():
            #create Rental object
            new_rental = Rental()
            new_rental.date = posted_Form.cleaned_data.get("date")

            #Compute start & endtime of rental
            duration = posted_Form.cleaned_data.get("duration")
            start = posted_Form.cleaned_data.get("time")
            temp = start
            end = temp.replace(hour=(start.hour + duration)% 24)

            new_rental.startTime = start
            new_rental.endTime = end

            #Compute Price Estimate for rental
            if duration == 24:
                total = theOne.day_Rate
            else:
                total = int(duration * theOne.hourly_Rate)

            new_rental.totalPrice = total


            #create message object
            new_message = Message()
            new_message.sender = request.user
            new_message.receiver = theOne.lister
            #new_message.receiver = 12 #TODO: Update Models.
            new_message.msg_content = posted_Form.cleaned_data.get("comment")

            #create Rental Item
            rental_Item = RentalItem()

            #Add Foreign Keys
            rental_Item.message = new_message
            rental_Item.rental = new_rental
            rental_Item.listing = theOne
            rental_Item.renter = request.user

            #Save Objects to Database
            new_rental.save()
            new_message.save()
            rental_Item.save()


        #display rental request in User's and Lister's inbox.
        return redirect('request')

    else:
        #load rental form date/time
        rForm = RentalForm()


    #send to listing_single.html
    return render(request,'rentals/rent_listing.html', {'listing': theOne, 'rental_form': rForm})






# Rental Request Demo View
#display confirmation to user/instructions of steps
class RequestedRentalView(TemplateView):
    template_name = 'rentals/rental_request.html'





'''
creating function for bookings/listings/
<input type="button" value="Submit" onClick="create_note();">
https://stackoverflow.com/questions/5735107/make-queries-from-javascript-to-django-server
'''

'''
DESERIALIZING JSON File in Python
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
    '''


'''
Fetching data from Foreign Key relationships

class A(models.Model): 
   pass
  
class B(models.Model): 
   a = ForeignKey(ModelA) 
  
  
# Forward ForeignKey relationship 
A.objects.select_related('a').all() 
  
# Reverse ForeignKey relationship 
A.objects.prefetch_related('modelb_set').all()  

'''

