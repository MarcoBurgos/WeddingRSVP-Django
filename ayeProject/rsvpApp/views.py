from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from . import forms
from rsvpApp.models import Guest, Invitation
from datetime import datetime, timedelta


# Create your views here.

def index(request):
    email_form = forms.EmailForm()
    guests_form = forms.GuestsForm()
    return render(request, 'rsvpApp/index.html', {'email_form': email_form, 'guests_form': guests_form})

def ajax_call(request):
    if request.method == 'GET':
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

    else:
        names_to_saved = request.POST.get('guests', None)
        invitation_size = names_to_saved.split(",")
        email = request.POST.get('email', None)
        emailID = Guest.objects.get(email__exact=email)

        guestRecord = Invitation.objects.get(invitation_owner_name__exact=emailID)
        guestRecord.guests_confirmed = names_to_saved
        guestRecord.total_guests_confirmed = len(invitation_size)
        guestRecord.is_RSVP = True
        guestRecord.date_RSVP = (datetime.now()) - (timedelta(hours=4, minutes=00))
        guestRecord.save()


        return HttpResponse("Success!")
