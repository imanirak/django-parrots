from django.shortcuts import render
from django.views import View 
from django.http import HttpResponse, HttpResponseRedirect #a class to handle sending http responses
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from .models import Parrot, ParrotSnacks
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

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
    

# parrots = [
#     Parrot("African Grey"),
#     Parrot("Cockatoos"),
#     Parrot("Macaws"),
#     Parrot("Parrotlet"),
#     Parrot("Cockatiel"),
#     Parrot("Senegal"),
#     Parrot("Parakeets"),
#     Parrot("Eclectus"),
#     Parrot("Amazon"),
#     Parrot("Pionus"),
#     Parrot("Conure"),
#     Parrot("Burrowing"),
#     Parrot("Caique"),
#     Parrot("Yellow-Naped Amazon"),
#     Parrot("Meyer's"),
#     Parrot("Ring-Necked Parakeet"),
#     Parrot("Kakariki"),
#     Parrot("Timneh Greys"),
#     Parrot("Quaker"),
#     Parrot("Lovebirds")
           
#            ]



class Parrot_List(TemplateView):
    template_name= 'parrot_list.html'

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        # context['parrots']=Parrot.objects.all()
        # return context
                # to get the query parameter we have to acccess it in the request.GET dictionary object  
        # If a query exists we will filter by name       
        if name != None:
            # .filter is the sql WHERE statement and name__icontains is doing a search for any name that contains the query param

            context["parrots"] = Parrot.objects.filter(name__icontains=name)
            context["header"] = f'Searching for {name}'
        else: 
            context["parrots"] = Parrot.objects.all() # this is where we add the key into our context object for the view to use
            context["header"] = "Our Parrots:"
        return context

    
class ParrotCreate(CreateView):
    model = Parrot
    fields = ['name', 'img','parrotsnacks']
    success_url = '/parrots'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/parrots')


class Parrot_Detail(DetailView):
    model = Parrot
    template_name = "parrot_detail.html"

class Parrot_Update(UpdateView):
    model = Parrot
    fields = ['name', 'img', 'parrotsnacks']
    template_name = "parrot_update.html"
    def get_success_url(self):
        return reverse('parrot_detail', kwargs={'pk': self.object.pk})

class Parrot_Delete(DeleteView):
    model = Parrot
    template_name = 'parrot_delete_confirmation.html'
    success_url = "/parrots/"

# add this new view function
def profile(request, username):
    user = User.objects.get(username=username)
    first_name = User.objects.get(first_name=user.first_name)
    parrots = Parrot.objects.filter(user=user)
    return render(request, 'profile.html', {'username':username, 'parrots': parrots, 'first_name':first_name} )


def parrotsnacks_index(request):
    parrotsnacks = ParrotSnacks.objects.all()
    return render(request, 'parrotsnacks_index.html', {'parrotsnacks':parrotsnacks})

def parrotsnacks_show(request, parrotsnack_id):
    parrotsnack = ParrotSnacks.objects.get(id=parrotsnack_id)
    return render(request, 'parrotsnacks_show.html', {'parrotsnack':parrotsnack})

class ParrotSnacksCreate(CreateView):
    model = ParrotSnacks
    fields = '__all__'
    template_name='parrotsnacks_form.html'
    success_url='/parrotsnacks'
    
class ParrotSnacksUpdate(UpdateView):
    model = ParrotSnacks
    fields = ['name']
    template_name = 'parrotsnacks_update.html'
    success_url='/parrotsnacks'

class ParrotSnacksDelete(DeleteView):
    model = ParrotSnacks
    template_name = 'parrotsnacks_confirm_delete.html'
    success_url = '/parrotsnacks'
