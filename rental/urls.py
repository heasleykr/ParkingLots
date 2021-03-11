from django.urls import path
from rental import views
from .views import RequestedRentalView, InboxView
from django.conf import settings


# Rental and Message paths
urlpatterns = [
    path('listings/', views.all_Listings, name='listings'),
    path('listings/loved', views.loved_Listings, name='loved_listings'),
    path('listings/prices', views.price_Listings, name='listings_prices'),
    path('listings/parking/<parking_type>',
         views.parking_Listings, name='listings_parking'),
    path('listings/vehicle/<vehicle_type>',
         views.vehicle_Listings, name='listings_vehicle'),
    path('listings/<listing_id>/', views.single_Listing, name='listing_single'),
    path('listings/<listing_id>/loved', views.save_Loved, name='loved_single'),
    path('listings/<loved_id>/', views.remove_Loved, name='loved_remove'),
    path('listings/<listing_id>/rent', views.rent_Listing, name='rent_listing'),
    path('rental_request/', RequestedRentalView.as_view(), name='request'),
    path('inbox/', InboxView.as_view(), name='inbox'),
    path('bookings/', views.all_Bookings, name='all_bookings'),
    path('<int:rental_id>/', views.single_Booking, name='single_booking'),
    path('<int:rental_Item_id>/confirm',
         views.confirm_Request, name='confirm_booking'),
    path('<int:rental_Item_id>/deny', views.deny_Request, name='deny_booking'),

]
