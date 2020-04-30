from django.contrib import admin
from rsvpApp.models import Guest, Invitation

# Register your models here.

class InvitationForm(admin.ModelAdmin):
    exclude = ('guests_confirmed', 'total_guests_confirmed', 'is_RSVP', 'date_RSVP',)



admin.site.register(Guest)
admin.site.register(Invitation, InvitationForm)
