from django.shortcuts import render,redirect
from bookings.models import Booking
from bookings.forms import BookingForm
# Create your views here.


def update(request,booking_id):
    '''saves a new booking'''
    if request.method == 'GET':
        print "Booking id: {0}".format(booking_id)
        booking_to_edit = Booking.objects.get(pk=booking_id)
        booking_form = BookingForm(instance=booking_to_edit)
        print "Form:\n {0}".format(booking_form.as_p())
        return render(request,'bookings/edit_booking.html',{'form':booking_form})
    if request.method == 'POST':
        print "Booking id: {0}".format(booking_id)
        booking_to_edit = Booking.objects.get(pk=booking_id)
        booking_form = BookingForm(request.POST,instance=booking_to_edit)
        booking_form.save()
        return redirect('home')
    return redirect('home')

def delete(request,booking_id):
    '''deletes a useless booking'''
    print "Booking id: {0}".format(booking_id)
    Booking.objects.get(pk=booking_id).delete()
    return redirect('home')
