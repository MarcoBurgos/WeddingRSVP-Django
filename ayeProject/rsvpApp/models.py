from django.db import models
from django.forms import ModelForm

# Create your models here.
class Invitation(models.Model):
    invitation_owner_name = models.CharField(max_length=90, verbose_name="Propietario de la invitación")
    email = models.EmailField(max_length = 128, unique=True)
    telephone = models.CharField(max_length=16)
    guest_names = models.CharField(max_length=256, verbose_name="Nombres de invitados")
    number_of_guests = models.IntegerField(verbose_name="Total de invitados")
    guests_confirmed = models.CharField(max_length=256, null=True, blank=True, verbose_name="Nombres confirmados")
    total_guests_confirmed = models.IntegerField(null=True, blank=True, verbose_name="Total de confirmados")
    is_RSVP = models.BooleanField(null=True, blank=True, verbose_name="¿Confirmó?")
    date_RSVP =models.DateField(null=True, blank=True, verbose_name="Fecha confirmación")

    def __str__(self):
        return str(self.guest_names)

    class Meta:
        verbose_name_plural = "Invitaciones"


# class Guest(models.Model):
#     invitation_owner_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length = 128, unique=True)
#     telephone = models.CharField(max_length=12)
#
#     def __str__(self):
#          return self.invitation_owner_name
#
#     class Meta:
#         verbose_name_plural = "Invitados"
#
# class Invitation(models.Model):
#     invitation_owner_name = models.ForeignKey(Guest, on_delete=models.CASCADE,
#     verbose_name="Seleccione el invitado con el cual relacionar la invitación")
#     guest_names = models.CharField(max_length=256)
#     number_of_guests = models.IntegerField()
#     guests_confirmed = models.CharField(max_length=256, null=True, blank=True)
#     total_guests_confirmed = models.IntegerField(null=True, blank=True)
#     is_RSVP = models.BooleanField(null=True, blank=True)
#     date_RSVP =models.DateField(null=True, blank=True)
#
#     def __str__(self):
#         return str(self.guest_names)
#
#     class Meta:
#         verbose_name_plural = "Invitaciones"
