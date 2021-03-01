from django.contrib.auth.models import AbstractUser 
from django.db import models

# Child of the AbstractBaseUser class 

# Create your models here.
# Verifiy if there's positive integer. Takes 'null' or no input
# Null: Databse-related. Meaning No value. Python uses 'None' class. 
# Blank: Validation-related. Allows an empty value in a form
# Together these can store and empty 'no value' in the DB. 
class CustomUser(AbstractUser):
        # first_name = models.CharField(max_length=32, help_text='First name')
        # last_name = models.CharField(max_length=32, help_text='Last name')
        # username = models.CharField(max_length=32, help_text='username/Login Id')
        # email = models.EmailField(max_length=64, help_text='Enter a valid email address')
        isLister = models.BooleanField(default=False, help_text='Will you be listingrenting your own parking spot?')
