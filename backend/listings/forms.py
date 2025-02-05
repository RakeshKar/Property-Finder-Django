# from django import forms
# from .models import Listing
# from django.contrib.gis.geos import Point

# class ListingsForm(forms.ModelForm):
#     class Meta:
#         model = Listing
#         #picture 1-5 means 5 pictures can be uploaded for a single property
#         fields = ['title', 'description', 'area', 'borough', 'listing_type', 'property_status', 'price', 'rental_frequency', 'rooms', 'furnished', 'pool', 'elevator', 'cctv', 'parking', 'date_posted', 'location', 'latitude', 'longitude', 'picture1', 'picture2', 'picture3', 'picture4', 'picture5']
     
#     #the goal here is to get the location field to get its value from the latitude and the longitude fields itself  
#     #so, use clean method
#     latitude = forms.FloatField()
#     longitude = forms.FloatField()

#     def clean(self):#argument is self
#         #store the form data in a variable called data
#         #the super method lets us have access to the form itself
#         data = super().clean()
#         #need to extract latitude and longitude from the data dictionary
#         latitude = data.pop('latitude')
#         longitude = data.pop('longitude')
#         #the data variable will be a dictionary with key value pairs and we get the location field from the latitude and longitude fields and it has to be a point object
#         data['location'] = Point(latitude, longitude, srid=4326)
#         return data

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         location = self.initial.get('location')
#         if isinstance(location, Point):
#             self.initial['latitude'] = location.tuple[0]
#             self.initial['longitude'] = location.tuple[1]
    
    
   