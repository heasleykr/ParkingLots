from django.shortcuts import render, redirect
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
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


#Display Inbox messages
class InboxView(ListView):
    model = Message
    template_name = 'bookings/inbox.html'


#renders all bookings for requested user
def all_Listings(request):

    if request.method == "GET":

        #Query DB: grab all listings
        list = Listing.objects.all()


    #send to listings.html
    return render(request,'all_listings.html', {'listings': list})

#Sorts listings by Price
def price_Listings(request):

    if request.method == "GET":

        #Query DB: grab all listings and sort ascending by hourly price
        prices = Listing.objects.order_by('hourly_Rate')


    #send to listings.html
    return render(request,'all_listings.html', {'listings': prices})

#Sorts listings by Parking Type
def parking_Listings(request, parking_type):

    if request.method == "GET":

        if parking_type == "r":

            #Query DB: grab all residential parking
            parkinglist = Listing.objects.filter(parking='R')

        elif parking_type == "g":

            #Query DB: grab all residential parking
            parkinglist = Listing.objects.filter(parking='G')

        elif parking_type == "l":

            #Query DB: grab all residential parking
            parkinglist = Listing.objects.filter(parking='L')

        elif parking_type == "s":

            #Query DB: grab all residential parking
            parkinglist = Listing.objects.filter(parking='S')

        elif parking_type == "o":

            #Query DB: grab all residential parking
            parkinglist = Listing.objects.filter(parking='O')

    #send to listings.html
    return render(request,'all_listings.html', {'listings': parkinglist})

#Sorts listings by Vehicle Accomidation
def vehicle_Listings(request, vehicle_type):

    if request.method == "GET":

        if vehicle_type == "c":

            #Query DB: grab all residential parking
            vehiclelist = Listing.objects.filter(vehicles='C')

        elif vehicle_type == "t":

            #Query DB: grab all residential parking
            vehiclelist = Listing.objects.filter(vehicles='T')

        elif vehicle_type == "v":

            #Query DB: grab all residential parking
            vehiclelist = Listing.objects.filter(vehicles='V')

        elif vehicle_type == "m":

            #Query DB: grab all residential parking
            vehiclelist = Listing.objects.filter(vehicles='M')

        elif vehicle_type == "o":

            #Query DB: grab all residential parking
            vehiclelist = Listing.objects.filter(vehicles='O')

    #send to listings.html
    return render(request,'all_listings.html', {'listings': vehiclelist})

#renders all bookings for requested user
def all_Bookings(request):

    if request.method == "GET":

        #Query DB: grab reguested bookings for user, both rentals and listings
        user_rented_Items = RentalItem.objects.filter(renter=request.user)

        user_Listed_Items = RentalItem.objects.filter(listing__lister=request.user)


    #send to bookings.html
    return render(request,'bookings/bookings.html', {'rented_Items': user_rented_Items, 'listed_Items': user_Listed_Items})


#renders single booking request with details
def single_Booking(request, rental_id):

    id = int(rental_id)

    if request.method == "GET":
        #grad reguested listing by id
        theRental = RentalItem.objects.get(pk=id)
        theListing = theRental.listing
        rental_details = theRental.rental

    #send to listing_single.html
    return render(request,'bookings/single_booking.html', {'rental_Item': theRental, 'rental': rental_details, 'listing': theListing})


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
            new_message.msg_content = posted_Form.cleaned_data.get("comment")

            #create Rental Item
            rental_Item = RentalItem()

            #Add Foreign Keys
            rental_Item.message = new_message
            rental_Item.rental = new_rental
            rental_Item.listing = theOne
            rental_Item.renter = request.user

            #Message Foreign Key assigments
            new_message.rentalItem_id = rental_Item.rental_Item_id
            new_message.listingItem_id = theOne

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

