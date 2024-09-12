from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bird, Feeding
from .forms import FeedingForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Bird, Sighting


class BirdList(LoginRequiredMixin, ListView):
    model = Bird
    template_name = 'birdcollectorapp/templates/bird_list.html'  # You'll create this template

class BirdDetail(LoginRequiredMixin, DetailView):
    model = Bird
    template_name = 'birds/bird_detail.html'

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
    template_name = 'birdcollectorapp/bird_form.html'  # Correct path to your template
    success_url = reverse_lazy('bird_list')


class BirdDelete(LoginRequiredMixin, DeleteView):
    model = Bird
    template_name = 'birds/bird_confirm_delete.html'
    success_url = reverse_lazy('bird-index')
# Create your views here.

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