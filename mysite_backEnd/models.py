from django.db import models
from phone_field import PhoneField
from django_countries.fields import CountryField

DATE_INPUT_FORMATS = ('%d-%m-%Y','%Y-%m-%d')

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    first_name = models.CharField(null=False,max_length=10)
    last_name = models.CharField(null=False,max_length=10)
    gender=models.CharField(max_length=6,choices= (('male', 'male'),('female', 'female')))
    birthDate=models.DateField(DATE_INPUT_FORMATS)
    password = models.CharField(null=False,max_length=200)
    phone_number= PhoneField(E164_only=True,blank=False,unique=True ,max_length=200)
    email = models.EmailField(null=False,unique=True,max_length=50)
    countryCode = CountryField(blank=False)
    picture_path= models.CharField(null=False,max_length=500)
