from django.urls import path
from . import views
from .views import home, about

urlpatterns = [
    path('', views.home, name='project'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('gallery/', views.gallery, name='gallery'),
]
