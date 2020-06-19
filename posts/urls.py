from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('post/<int:pk>/', views.post_view, name='post_view'),
]