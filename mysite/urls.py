from django.urls import path
from .views import home_view, about_view,service_view,why_view,register_view


urlpatterns = [
    path('',home_view,name='home-page'),
    path('about/',about_view,name='about-page'),
    path('service/',service_view,name='service-page'),
  
    path('why/',why_view,name='why-page'),
   path('register',register_view, name="register-page")
]
