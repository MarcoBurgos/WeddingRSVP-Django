from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import forms
from rsvpApp.models import Guest, Invitation


# Create your views here.

def index(request):
    email_form = forms.EmailForm()
    guests_form = forms.GuestsForm()
    return render(request, 'rsvpApp/index.html', {'email_form': email_form, 'guests_form': guests_form})

def validate_guest(request):
    email = request.GET.get('email', None)
    data = {
         'is_there': Guest.objects.filter(email__exact=email).exists()
     }
    if data['is_there']:
        emailID = Guest.objects.get(email__exact=email)
        data['guests'] = Invitation.objects.get(invitation_owner_name = emailID).guest_names
        data['name'] = Guest.objects.get(email = email).invitation_owner_name
        data['no_of_guests'] = Invitation.objects.get(invitation_owner_name = emailID).number_of_guests

    else:
        data['error_message'] = 'No existe el correo ingresado en la base de datos.'


    print(str(data))

    return JsonResponse(data)

def save_guest_into_db(request):
     names_to_saved = request.GET.get('guests', None)
     print(names_to_saved)
