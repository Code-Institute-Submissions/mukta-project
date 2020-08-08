from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Workshop

# Create your views here.


class WorkshopListView(ListView):
    model = Workshop
    template_name = 'workshops/workshops.html'
    context_object_name = 'workshops'


class WorkshopDetailView(DetailView):
    model = Workshop
    template_name = 'workshops/workshop-detail.html'
    context_object_name = 'workshop-detail'


class WorkshopCreateView(CreateView):
    model = Workshop
    template_name = 'workshops/workshop-form.html'
    context_object_name = 'workshop-create'
    fields = ['title', 'date', 'location',
              'time', 'instructor', 'content', 'images']
    success_url = '/workshops'

    def form_valid(self, form):
        return super().form_valid(form)
