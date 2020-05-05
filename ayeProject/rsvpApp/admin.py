from django.contrib import admin
from rsvpApp.models import Guest, Invitation

# Register your models here.

class InvitationForm(admin.ModelAdmin):

    fields = ['invitation_owner_name', 'guest_names', 'number_of_guests', 'guests_confirmed', 'total_guests_confirmed', 'is_RSVP', 'date_RSVP']
    #exclude = ('guests_confirmed', 'total_guests_confirmed', 'is_RSVP', 'date_RSVP',)
    #search_fields = ['invitation_owner_name']

    list_filter = ['is_RSVP']

    list_display = ['invitation_owner_name', 'guest_names', 'number_of_guests', 'guests_confirmed', 'total_guests_confirmed', 'is_RSVP', 'date_RSVP']



admin.site.register(Guest)
admin.site.register(Invitation, InvitationForm)
