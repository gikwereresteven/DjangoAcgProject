from django.urls import path

from . import views

urlpatterns = [  
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('imbuto', views.imbuto, name='imbuto'),
    path('imishwi', views.imishwi, name='imishwi'),
    path('ifumbire', views.ifumbire, name='ifumbire'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    
]