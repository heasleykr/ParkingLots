from django.urls import path
from rental import views
from .views import RequestedRentalView
from django.conf import settings


#SignUp View
urlpatterns = [
    path('listings/', views.send_Listings, name='listings'),
    path('listings/<listing_id>/', views.single_Listing, name='listing_single'),
    path('listings/<listing_id>/rent', views.rent_Listing, name='rent_listing'),
    path('rental_request/', RequestedRentalView.as_view(), name='request'),

]


