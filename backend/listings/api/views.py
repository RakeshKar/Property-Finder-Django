from .serializers import ListingSerializer
from listings.models import Listing

#easy way of creating view is using djangorestframework generic views
from rest_framework import generics

class ListingList(generics.ListAPIView):
    #what we want to show, by default a query set
    #order_by date posted meaning in the listings.js page, new listing cards will show first, then the older ones
    queryset = Listing.objects.all().order_by('-date_posted')
    #which serialization we want to use
    serializer_class = ListingSerializer
    
    #for posting the AddProperty page's form info in backend
class ListingCreate(generics.CreateAPIView):
    #what we want to show, by default a query set
    queryset = Listing.objects.all()
    #which serialization we want to use
    serializer_class = ListingSerializer
    
#This is all we need to create a view that will show all the property listings in JSON format

class ListingDetail(generics.RetrieveAPIView):
    #what we want to show, by default a query set
    queryset = Listing.objects.all()
    #which serialization we want to use
    serializer_class = ListingSerializer
    
#To delete the particular listing if logged in as the user(who uploaded the listing)
class ListingDelete(generics.DestroyAPIView):
    #what we want to show, by default a query set
    queryset = Listing.objects.all()
    #which serialization we want to use
    serializer_class = ListingSerializer
    
#To update the particular listing if logged in as the user(who uploaded the listing)
class ListingUpdate(generics.UpdateAPIView):
    #what we want to show, by default a query set
    queryset = Listing.objects.all()
    #which serialization we want to use
    serializer_class = ListingSerializer