from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name = 'contact'),
    path('service/', views.service, name = 'service'),
    path('project/', views.project, name ='project'),
    
    
]
