from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Bird

class BirdList(ListView):
    model = Bird
    template_name = 'birds/bird_list.html'  # You'll create this template

class BirdDetail(DetailView):
    model = Bird
    template_name = 'birds/bird_detail.html'

class BirdCreate(CreateView):
    model = Bird
    fields = ['name', 'species', 'age', 'description']  # Add necessary fields
    template_name = 'birds/bird_form.html'
    success_url = reverse_lazy('bird-index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BirdUpdate(UpdateView):
    model = Bird
    fields = ['name', 'species', 'age', 'description']
    template_name = 'birds/bird_form.html'
    success_url = reverse_lazy('bird-index')

class BirdDelete(DeleteView):
    model = Bird
    template_name = 'birds/bird_confirm_delete.html'
    success_url = reverse_lazy('bird-index')
# Create your views here.
