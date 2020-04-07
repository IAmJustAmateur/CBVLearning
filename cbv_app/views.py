from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from cbv_app.models import School, Student

# Create your views here.
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'cbv_app/school_detail.html'
