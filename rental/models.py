from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse

# Addtional imports
from parking.models import Listing
import uuid


# Rental Model
class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    totalPrice = models.DecimalField(max_digits=6, decimal_places=2)

    # Confirmation Number: UUID(Universaly Unique Identifiers)
    confirmationNumber = models.UUIDField(
        default=uuid.uuid4, unique=True, db_index=True, editable=False)

    # Forced property for VS Code // Django adds dynamically
    objects = models.Manager()

    def __str__(self):
        return str(self.rental_id)

# Message Model
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver")
    msg_content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # Foreign Key
    rentalItem_id = models.IntegerField(null=True, blank=True)

    listingItem_id = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='listing')

    # Forced property for VS Code // Django adds dynamically
    objects = models.Manager()

    def __str__(self):
        return str(self.message_id)

    def get_absolute_url(self):
        return reverse('single_message', args=[str(self.message_id)])


# Rental Item Model 
class RentalItem(models.Model):

    ############## DB Fields #############################
    rental_Item_id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    cancel_reason = models.TextField(null=True, blank=True)
    cancelled = models.BooleanField(default=False)
    confirmed = models.BooleanField(default=False)

    # key connections
    message = models.ForeignKey(
        Message, on_delete=models.CASCADE, related_name='message')
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    renter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Forced property for VS Code // Django adds dynamically
    objects = models.Manager()

    def __str__(self):
        return str(self.rental_Item_id)

# Holds user's 'loved' rental listings
class LovedRentals(models.Model):
    ############## DB Fields #############################
    loved_id = models.AutoField(primary_key=True)
    listing = models.ForeignKey(
        Listing, on_delete=models.PROTECT, related_name='loved')
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
    )
