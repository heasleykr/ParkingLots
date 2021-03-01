from django.urls import path
from .views import HomePageView, ListingSuccess
from parking import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('list/images', views.add_Listing_2, name='listing_images'),
    path('list/<img_obj>/', views.add_Listing_5, name='listing_create'),
    path('preview/<img_obj>/<listing_body>/<listing_address>/', views.preview_Listing, name='listing_preview'),
    path('listed/', ListingSuccess.as_view(), name='listing_success'),
    path('search/', views.mapPageView, name='map'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
