from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact_view'),
    path('about/', views.about_view, name='about_view'),
    path('<int:pk>/', views.post_view, name='detail'),
    path('tag/', views.tag_view, name='tag_cloud'),
    path('tag/<tag>/', views.PostTaggedObjectList.as_view(), name='tagged_object_list'),
]