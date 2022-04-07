from pipes import Template
from django.shortcuts import render
from django.urls import path
from . import views

from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView

# Create your views here.


# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name ='home.html'
    # Here we are adding a method that will be ran when we are dealing with a GET request
    # def get(self, request):
    #     # Here we are returning a generic response
    #     # This is similar to response.send() in express
    #     return HttpResponse("Welcome Parrots!!")
    
class About(TemplateView):
    template_name='about.html'
    
class Parrot:
    def __init__(self, name):
        self.name = name
    

parrots = [
    Parrot("African Grey"),
    Parrot("Cockatoos"),
    Parrot("Macaws"),
    Parrot("Parrotlet"),
    Parrot("Cockatiel"),
    Parrot("Senegal"),
    Parrot("Parakeets"),
    Parrot("Eclectus"),
    Parrot("Amazon"),
    Parrot("Pionus"),
    Parrot("Conure"),
    Parrot("Burrowing"),
    Parrot("Caique"),
    Parrot("Yellow-Naped Amazon"),
    Parrot("Meyer's"),
    Parrot("Ring-Necked Parakeet"),
    Parrot("Kakariki"),
    Parrot("Timneh Greys"),
    Parrot("Quaker"),
    Parrot("Lovebirds")
           
           ]

class Parrot_List(TemplateView):
    template_name= 'parrot_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['parrots'] = parrots
        
        return context