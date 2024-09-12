from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bird

class BirdList(LoginRequiredMixin, ListView):
    model = Bird
    template_name = 'bird/bird_list.html'  # You'll create this template

class BirdDetail(LoginRequiredMixin, DetailView):
    model = Bird
    template_name = 'birds/bird_detail.html'

class BirdCreate(LoginRequiredMixin, CreateView):
    model = Bird
    fields = ['name', 'species', 'age', 'description']  # Add necessary fields
    template_name = 'birds/bird_form.html'
    success_url = reverse_lazy('bird-index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BirdUpdate(LoginRequiredMixin, UpdateView):
    model = Bird
    fields = ['name', 'species', 'age', 'description']
    template_name = 'birds/bird_form.html'
    success_url = reverse_lazy('bird-index')

class BirdDelete(LoginRequiredMixin, DeleteView):
    model = Bird
    template_name = 'birds/bird_confirm_delete.html'
    success_url = reverse_lazy('bird-index')
# Create your views here.

class SightingCreate(LoginRequiredMixin, CreateView):
    model = Sighting
    fields = ['date', 'location']
    template_name = 'sightings/sighting_form.html'
    success_url = reverse_lazy('bird-index')

    def form_valid(self, form):
        form.instance.bird = Bird.objects.get(id=self.kwargs['pk'])  # Get the bird related to the sighting
        return super().form_valid(form)
