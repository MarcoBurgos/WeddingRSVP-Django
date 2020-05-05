from django.urls import path
from rsvpApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax_call/', views.ajax_call, name='email_form_view')
 ]
