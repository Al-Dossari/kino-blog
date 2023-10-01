from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    photo = models.ImageField(upload_to=f'accounts/profile_photo/',null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True,verbose_name="Адрес")
    phone_number = PhoneNumberField(null=True,blank=True,verbose_name='Телефон')
