from django.db import models
from django.forms import ModelForm

# Create your models here.
class Guest(models.Model):
    invitation_owner_name = models.CharField(max_length=50)
    email = models.EmailField(max_length = 128, unique=True)
    telephone = models.CharField(max_length=12)

    def __str__(self):
         return self.invitation_owner_name

    class Meta:
        verbose_name_plural = "Invitados"

class Invitation(models.Model):
    invitation_owner_name = models.ForeignKey(Guest, on_delete=models.CASCADE,
    verbose_name="Relacionar con invitado",)
    guest_names = models.CharField(max_length=256)
    number_of_guests = models.IntegerField()
    guests_confirmed = models.CharField(max_length=256, null=True)
    total_guests_confirmed = models.IntegerField(null=True)
    is_RSVP = models.BooleanField(null=True)
    date_RSVP =models.DateField(null=True)

    def __str__(self):
        return str(self.guest_names)

    class Meta:
        verbose_name_plural = "Invitaciones"


class GuestForm(ModelForm):
    class Meta:
        model = Guest
        fields = ['invitation_owner_name', 'email', 'telephone']


class GuestForm(ModelForm):
    class Meta:
        model = Invitation
        fields = ['guest_names', 'number_of_guests']
        exclude = ('guests_confirmed', 'total_guests_confirmed', 'is_RSVP', 'date_RSVP',)
