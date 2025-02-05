from django.contrib import admin
#for getting the listing model in the localhost:8000/admin (django page)
from listings.models import Listing
# from .forms import ListingsForm

#in order to modify the form in the admin panel, we need to create a new admin class
# class ListingAdmin(admin.ModelAdmin):
#     form = ListingsForm

# Register your models here.

admin.site.register(Listing)
