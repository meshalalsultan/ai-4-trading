from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('bitcoin/', views.bitcoin , name='bitcoin'),
    path('prices/', views.prices , name='prices'),
    path('bit/', views.bit , name='bit'),
]
