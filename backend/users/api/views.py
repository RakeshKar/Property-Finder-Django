from users.models import Profile
from .serializers import ProfileSerializer
from rest_framework import generics

#we want to create a view for every single profile
class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    
#we want to create a view for every single profile
class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #in localhost:8000/api/profiles/ the id given is of seller, which is not userId, to give userId, we use lookup_field
    lookup_field = 'seller'
    
#want to update the existing profile
class ProfileUpdate(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    #in localhost:8000/api/profiles/ the id given is of seller, which is not userId, to give userId, we use lookup_field
    lookup_field = 'seller'