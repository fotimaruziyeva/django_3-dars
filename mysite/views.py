from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Team

def home_view(request):
 return render(request=request,template_name='index.html')

def about_view(request):
 return render(request=request,template_name='about.html')


def service_view(request):
 return render(request=request,template_name='service.html')



def why_view(request):
 return render(request=request,template_name='why.html')

def register_view(request):
 return render(request=request,template_name='register.html')


