from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact_view'),
    path('about/', views.about_view, name='about_view'),
]