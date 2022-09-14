# from unicodedata import name
# from curses import keyname
from django.shortcuts import render
from detail.models import comment
# from django.contrib.auth.decorators import login_required
from app1.models import FREE_CONSULATION
from django.contrib import messages
from app1.models import email_address
from django.http import HttpResponse
# Create your views here.

def index (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        email = request.POST.get('email')

        if name and phone and message :
           f = FREE_CONSULATION.objects.create(name = name, phone =  phone , message = message)
           f.save()
           return render (request, 'app1/index.html',{})
        
        elif email :
            em = email_address.objects.create(email = email)
            em.save()
            return render ( request ,'app1/contact.html', {})
    elif request.method =='GET':
      
        return render (request, 'app1/index.html',{})
# ================================================================================

def about (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        email = request.POST.get ('email')
        if name and phone and message :
           f = FREE_CONSULATION.objects.create(name = name, phone =  phone , message = message)
           f.save()
           return render (request, 'app1/about.html',{})
        elif email:
            em = email_address.objects.create(email = email)
            em.save()
        return render ( request ,'app1/contact.html', {})
    elif request.method =='GET':
        return render (request, 'app1/about.html',{})

# ====================================================================================
def blog (request):
    if request.method == 'POST':
        email = request.POST.get ('email')
        if email:
            em = email_address.objects.create(email = email)
            em.save()
            return render ( request ,'app1/contact.html', {})
    elif request.method == 'GET':
        g = comment.objects.all()
        return render (request, 'app1/blog.html',{'g':g})
# ======================================================================================================================
def contact (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('text')
        message = request.POST.get('message')
        
        
        if name and email and text and message :
            s = comment.objects.create(name = name , email = email , text = text , message = message )
            s.save()
            return render(request, 'app1/contact.html',{})
        elif email:
            em = email_address.objects.create(email = email)
            em.save()
            return render ( request ,'app1/contact.html', {})

    elif request.method =='GET':
        return render (request, 'app1/contact.html',{})
        

# ==============================================================================================

def project (request):
    if request.method == 'POST':
       
        email = request.POST.get ('email')
        
        if email:
            em = email_address.objects.create(email = email)
            em.save()
            return render ( request ,'app1/contact.html', {})
    elif request.method == 'POST':
        return render (request, 'app1/project.html',{})
# ===============================================================================================
def service (request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        email = request.POST.get ('email')
        if name and phone and message :
           f = FREE_CONSULATION.objects.create(name = name, phone =  phone , message = message)
           f.save()
           return render (request, 'app1/service.html',{})
        elif email :
            em = email_address.objects.create(email = email)
            em.save()
            return render ( request ,'app1/contact.html', {})
    elif request.method =='GET':
        return render (request, 'app1/service.html',{})

    
    

