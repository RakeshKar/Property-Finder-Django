from rest_framework import serializers
from listings.models import Listing

class ListingSerializer(serializers.ModelSerializer):
    
    #adding country name (hardcode) and username of the seller to be in listing api
    country = serializers.SerializerMethodField()
    seller_username = serializers.SerializerMethodField()
    seller_agency_name = serializers.SerializerMethodField()
    
    #for accessing the seller's agency name from the frontend
    def get_seller_agency_name(self, obj):
        return obj.seller.profile.agency_name
    
    def get_seller_username (self, obj):
        return obj.seller.username
    
    def get_country(self, obj):
        return "Bangladesh"
    
    class Meta:
        #giving the model we want to serialize
        model = Listing
        #defining fields we want to serialize
        fields = '__all__'