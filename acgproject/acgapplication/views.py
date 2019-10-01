from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Post
from django.views.generic import View
from django.http import HttpResponse # Add this

from .forms import ContactForm # Add this


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def imbuto(request):
    return render(request, 'acgapplication/imbuto.html', {imbuto: 'imbuto'})

# Vertical menus of services  

def imishwi(request):
    return render(request, 'acgapplication/imishwi.html',{imishwi: 'imishwi'})

def ifumbire(request):
    return render(request, 'acgapplication/ifumbire.html',{ifumbire: 'ifumbire'})

# Horizontal menus services 

def home(request):
    return render(request,'acgapplication/home.html', {home:'home'})

def about(request):
    return render(request, 'acgapplication/about.html', {about:'about'})
      

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
          return render(request,'acgapplication/contact.html', {'contact':form})
    else:
        form = ContactForm()

   
    return render(request,'acgapplication/contact.html', {'form':form})

# def postform(request):
    
#     if request.method == 'POST':
#         if request.POST.get('name') and request.POST.get('email') and request.POST.get('message'):
#             post = Post()
#             post.name = request.POST('name')
#             post.email = request.POST('email')
#             post.name = request.POST('message')
#             post.save()
          
        
#         else:
#             return render(request,'acgapplication/contact.html', {'form': form})
            

