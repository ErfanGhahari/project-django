
from django.shortcuts import render
from .models import comment
from app1.models import email_address
from django.contrib import messages

# Create your views here.

def blogdetail (request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        message = request.POST.get('message')
        picture = request.POST.get('picture')


        if name and email and text and message :
            s = comment.objects.create(name = name , email = email , text = text , message = message ,picture = picture)
            s.save()
            return render(request, 'detail/blog-detail.html',{})
        elif email:
            em = email_address.objects.create(email = email)
            em.save()
            return render(request, 'detail/contact',{})
    elif request.method =='GET':
        return render (request, 'detail/blog-detail.html',{})
        

def projectdetails (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email :
            em = email_address.objects.create(email = email)
            em.save()
            return render (request, 'detail/project-details.html',{})
    elif request.method == 'GET':
        return render (request, 'detail/project-details.html',{})

def servicedetail (request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email :
            em = email_address.objects.create(email = email)
            em.save()
            return render (request, 'detail/contact.html',{})
    elif request.method == 'GET':
        return render (request, 'detail/service-detail.html',{})
    
