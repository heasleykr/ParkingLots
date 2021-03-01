from django.shortcuts import render, reverse, redirect
from django.views.generic import TemplateView, CreateView
from django.conf import settings
from django.urls import reverse_lazy
from .forms import ListingForm, ImageForm, AddressForm
from .models import Listing, Images, Address
from django.db import models


# HomeView
class HomePageView(TemplateView):
    template_name = 'home.html'



#Final Preview View For Lister: Imgage/Address/Listing pk's passed in
def preview_Listing(request, img_obj, listing_body, listing_address):

    if request.method == "POST":

        print("Posting preview")
        return redirect('home')

    else:
        #Query DB, return Obj
        image = Images.objects.get(images_id=int(img_obj))
        address = Address.objects.get(address_id=int(listing_address))
        listing = Listing.objects.get(listing_id=int(listing_body))

    
    return render(request,'listings/listing_preview.html', {'listing_body': listing, 'listing_address': address, 'img_obj': image})


#Success View for Listing
class ListingSuccess(TemplateView):
    template_name = 'listings/listing_success.html'



#Single: Image View Upload
def add_Listing_2(request):
    if request.method == "POST":
        #Image forms
        iForm = ImageForm(request.POST, request.FILES, instance=Images())

        if iForm.is_valid():
            #Object Save
            new_images = iForm.save()

            #grab object
            img_obj = new_images

            return redirect('listing_create', img_obj=img_obj, permanent=True)
  
    else:
        # Render empty image form
        iForm = ImageForm(instance=Images())

    return render(request,'listings/listing_images.html', {'images_form': iForm})


#Map View
def mapPageView(request):
    print(settings.GOOGLE_MAPS_API_KEY)
    context = {
        "APIKEY": settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'map_view.html', context)
    


# 2nd Listing Create: Address & Listing Combined / Image Instance passed in 
def add_Listing_5(request, img_obj):

    img_instance = img_obj
    print(img_obj)

    if request.method == "POST":
        #Address/Listing Forms
        lForm = ListingForm(request.POST, instance=Listing())
        aForm = AddressForm(request.POST, instance=Address())


        if lForm.is_valid() and aForm.is_valid():
            #Object Saves
            new_address = aForm.save()
            new_listing = lForm.save(commit=False) #don't save to DB yet


            #Add Foreign Keys
            # new_listing.address = new_address.instance
            new_listing.address = new_address
            print(new_address)

            #Query DB, return Image obj
            image = Images.objects.get(images_id=int(img_instance))

            #Set lister 
            new_listing.lister = request.user

            new_listing.images = image

            #save listing. 
            new_listing.save()


            return redirect('listing_preview', listing_address=new_address, listing_body=new_listing, img_obj=image, permanent=True)


    else:
        lForm = ListingForm(instance=Listing())
        aForm = AddressForm(instance=Address())

    
    return render(request,'listings/listing_create.html', {'listing_form': lForm, 'address_form': aForm})

    