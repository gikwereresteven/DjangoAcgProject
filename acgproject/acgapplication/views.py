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
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            submitted =True
           
            form = ContactForm()
            # send email code goes here
        return render(request,'acgapplication/contact.html', {'form':form, 'submitted': submitted})
    else:
        form = ContactForm()
    return render(request,'acgapplication/contact.html', {'form':form})

            

