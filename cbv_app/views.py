from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView,
                                    DetailView, CreateView, UpdateView, DeleteView)
from django.http import HttpResponse
from cbv_app.models import School, Student
from django.urls import reverse, reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'cbv_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = School
    fields = ('name', 'principal', 'location')

class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name', 'principal')

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("cbv_app:list")
