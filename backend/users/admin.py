from django.contrib import admin
from .models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()

#Registering models here
admin.site.register(User)
#after migration of models.py, to add profile in the admin panel
admin.site.register(Profile)