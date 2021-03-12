from django.contrib.auth.models import AbstractUser 
from django.db import models



# Create your models here.

class CustomUser(AbstractUser):
        isLister = models.BooleanField(default=False, help_text='Will you be listingrenting your own parking spot?')
