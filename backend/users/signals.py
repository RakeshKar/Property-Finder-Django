#goal: making profile automatically for each new user
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()
#every time a user is created, a signal is fired (post_save signal)


#the receiver ofthe signal added as a decorator
@receiver(post_save, sender=User)


#a user model, this sends a signal everytime a new user is created. That signal must have a receiver, when the receiver receives the signal, we do 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        #debug print. remove it
        print("User profile created for:", instance.username)
        Profile.objects.create(seller=instance) 
        
#after creating, now saving
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
        
        
##########
#what this file does:::
#when a user is saved (created) the user model sends a post_save signal to the receiver, who performs a task. The task is to create a profile function
#the arguments of the create_user_profile function are coming from post_save. After being created, the object will be created, and then Saved.
