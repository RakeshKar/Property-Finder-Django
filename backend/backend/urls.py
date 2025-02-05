"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#later we will import all the views from all the apps. So give each one an alias.
from listings.api import views as listings_api_views
#for forcing user to enter phone no and agency name
from users.api import views as users_api_views

#for serving images to the frontend
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', listings_api_views.ListingList.as_view()),
    #creating an endpoint(url) that will be used by AddProperty page to add property details in the backend
    path('api/listings/create/', listings_api_views.ListingCreate.as_view()),
    
    #creating api for getting details of each listing individually by id
    path('api/listings/<int:pk>/', listings_api_views.ListingDetail.as_view()),
    
     #creating api for deleting each listing individually by id
    path('api/listings/<int:pk>/delete/', listings_api_views.ListingDelete.as_view()),
    
    #creating api for updating each listing individually by id
    path('api/listings/<int:pk>/update/', listings_api_views.ListingUpdate.as_view()),
    
    path('api/profiles/', users_api_views.ProfileList.as_view()),
    #we are going to access a single profile by an ID(integer type), so <int:pk>, here pk is primary key
    path('api/profiles/<int:seller>/', users_api_views.ProfileDetail.as_view()),
    
    #for updating the existing profile
    path('api/profiles/<int:seller>/update/', users_api_views.ProfileUpdate.as_view()),
 
    #need a path for URL that will show all the property listings in JSON format (previous line)
    #for djoser token based authentication
    #this is the api of djoser where users unknowingly send their requests to when they try to register or login.
    path('api-auth-djoser/', include('djoser.urls')),
    path('api-auth-djoser/', include('djoser.urls.authtoken')),
    #(next line) for serving images to the frontend
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
