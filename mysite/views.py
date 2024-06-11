from django.shortcuts import render



def home_view(request):
 return render(request=request,template_name='index.html')

def about_view(request):
 return render(request=request,template_name='about.html')


def service_view(request):
 return render(request=request,template_name='service.html')



def team_view(request):
 return render(request=request,template_name='team.html')


def why_view(request):
 return render(request=request,template_name='why.html')

