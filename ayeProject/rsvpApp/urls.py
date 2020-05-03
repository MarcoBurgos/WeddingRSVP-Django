from django.urls import path
from rsvpApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('validate_guest/', views.validate_guest, name='email_form_view'),
    path('save_guest_into_db/', views.save_guest_into_db, name='guests_form_view')
 ]
