from django.db import models

# Create your models here.
#to customize the user model by adding new required field (email)
#so I need to access the user model
from django.contrib.auth.models import AbstractUser

#adding new field to the user
#by this, we will have access to the user
class User(AbstractUser):#the user class will inherit the properties of Abstractuser
    email = models.EmailField(unique=True)
  
#For having access of the profile. for adding profile page. each will be associated with each user, so oneToOne relation.
#CASCADE meaning if the user is deleted, then the profile will also be deleted  
#class profile will inherit from models.Model

class Profile(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE)
    agency_name = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=25, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    #the profile picture will be kept in folders having respected dates
    profile_picture = models.ImageField(
        upload_to='profile_pictures/%Y/%m/%d/', null=True, blank=True)
    
    #string method for this model, to return in string format, return f
    def __str__(self):
        return f"Profile of {self.seller.username}"