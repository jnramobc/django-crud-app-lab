from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bird, Feeding
from .forms import FeedingForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Bird, Sighting
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class BirdList(ListView):
    model = Bird
    template_name = 'birdcollectorapp/templates/bird_list.html'  # You'll create this template

class BirdDetail(LoginRequiredMixin, DetailView):
    model = Bird
    template_name = 'birds/bird_detail.html'  # Make sure this path matches the template location


class BirdCreate(LoginRequiredMixin, CreateView):
    model = Bird
    fields = ['name', 'species', 'description']  # Add necessary fields
    template_name = 'birdcollectorapp/bird_form.html'
    success_url = reverse_lazy('bird_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BirdUpdate(LoginRequiredMixin, UpdateView):
    model = Bird
    fields = ['name', 'species', 'description']
    template_name = 'birdcollectorapp/bird_form.html'  
    success_url = reverse_lazy('bird_list')

class BirdDelete(LoginRequiredMixin, DeleteView):
    model = Bird
    template_name = 'birdcollectorapp/bird_confirm_delete.html'  # Correct template path
    success_url = reverse_lazy('bird_list')


class SightingCreate(LoginRequiredMixin, CreateView):
    model = Sighting
    fields = ['date', 'location']
    template_name = 'birdcollectorapp/sighting_form.html'
    success_url = reverse_lazy('bird_list')

    def form_valid(self, form):
        form.instance.bird = Bird.objects.get(id=self.kwargs['pk'])  # Get the bird related to the sighting
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bird'] = Bird.objects.get(pk=self.kwargs['pk'])  # Pass bird to template
        return context
    
    from django.views.generic import ListView, DetailView

# List view to show all sightings
class SightingList(LoginRequiredMixin, ListView):
    model = Sighting
    template_name = 'sightings/sighting_list.html'

# Detail view for an individual sighting
class SightingDetail(LoginRequiredMixin, DetailView):
    model = Sighting
    template_name = 'sightings/sighting_detail.html'

# Update view for a sighting
class SightingUpdate(LoginRequiredMixin, UpdateView):
    model = Sighting
    fields = ['date', 'location']
    template_name = 'sightings/sighting_form.html'
    success_url = reverse_lazy('sighting-list')

# Delete view for a sighting
class SightingDelete(LoginRequiredMixin, DeleteView):
    model = Sighting
    template_name = 'sightings/sighting_confirm_delete.html'
    success_url = reverse_lazy('sighting-list')