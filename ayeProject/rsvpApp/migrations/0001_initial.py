# Generated by Django 3.0.3 on 2020-04-29 01:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invitation_owner_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=128, unique=True)),
                ('telephone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_names', models.CharField(max_length=256)),
                ('number_of_guests', models.IntegerField()),
                ('guests_confirmed', models.CharField(max_length=256)),
                ('total_guests_confirmed', models.IntegerField()),
                ('is_RSVP', models.BooleanField()),
                ('date_RSVP', models.DateField()),
                ('invitation_owner_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rsvpApp.Guest', verbose_name='the related to the Guests')),
            ],
        ),
    ]
