from django.contrib import admin
from django.urls import path
from .views import blogdetail , projectdetails , servicedetail


urlpatterns = [
    path('blog-detail/', blogdetail, name='blog-detail'),
    path('project-details/', projectdetails, name='project-details'),
    path('service-detail/', servicedetail, name = 'service-detail'),
    
]