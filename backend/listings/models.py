from random import choices
from django.contrib.gis.db import models
#for the models are not from django.db
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model
User = get_user_model()#this and above line are from admin.py file, as we have changed the default user model

    
#we can handle the user profiles here, but we will have separate app for handling the user profiles



# Create your models here.
class Listing(models.Model):
#class Listing is inheriting from models.Model
    #setting up a database table for the property listings of the application

    seller = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)#seller can sell multiple property. Sellers are also user. When the user account is deleted, all the listings of the seller is also deleted.
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    #choices_area is the tuple of the tuples
    choices_area = (
        ('Rajshahi', 'Rajshahi'),
        ('Dhaka', 'Dhaka'),
    )
    area = models.CharField(max_length=20, blank=True, null=True, choices=choices_area)
    borough = models.CharField(max_length=50, blank=True, null=True)
    #choices of borough is set up with react
    choices_listing_type = (
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Office', 'Office'),
    )
    
    listing_type = models.CharField(max_length=20, choices=choices_listing_type)
    
    choices_property_status = (
        ('Sale', 'Sale'),
        ('Rent', 'Rent'),
    )    
    
    property_status = models.CharField(max_length=20, blank=True, null=True, choices=choices_property_status)
    price = models.DecimalField(max_digits=50, decimal_places=0)
    choices_rental_frequency = (
        ('Month', 'Month'),
        ('Week', 'Week'),
        ('Day', 'Day'),
    )
    rental_frequency = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_rental_frequency)
    rooms = models.IntegerField(blank=True, null=True)
    bachelorallow = models.BooleanField(default=False)
    securityguard= models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    #timezone.now => date posted equal to whatever time the user posted the ad (either admin of the site or the end user)
    #for this to work, need timezone util from django
    date_posted = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    #to make the coordinates represented as lattitude and longitude, we use as property called SRID
    #SRID=special reference Idendentifier (need to set it to 4326, as it is the most common identifier, which reprents spatial data by using lattitude and longitude)
    #pointfield is imported from geos, which is a geometry engine
    
    
    #for adding the pictures in the listings page. Also, we use upload_to argument for uploading the picture in the media folder with specific date after each listing with image is created in the admin panel
    picture1 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    #here, we give the option to have 5 pictures of a single property
    picture2 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture3 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture4 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    picture5 = models.ImageField(blank=True, null=True, upload_to="pictures/%Y/%m/%d/")
    
    #giving name of the created Listing object
    def __str__(self):
        return self.title
    
    
    
    
    