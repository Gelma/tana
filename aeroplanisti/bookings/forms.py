from django.forms import ModelForm
from bookings.models import Booking

class BookingForm(ModelForm):
    '''the form for bookings editing'''
    class Meta:
        model=Booking
