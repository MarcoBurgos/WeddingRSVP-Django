from django.urls import path
from rsvpApp import views

urlpatterns = [
    path('', views.index, name='index')
 ]
