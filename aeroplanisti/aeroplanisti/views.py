from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth import authenticate, login
from bookings.models import Booking
import sys
# Create your views here.

def home(request):
    '''the home request, should show app home page'''
    today = datetime.now()
    if request.method=='GET':
        bookings = Booking.objects.all()
        return render(request,'home.html',{'today':today,'bookings':bookings});
    if request.method =='POST':
        try:
            my_date=request.POST['date']
            my_name=request.POST['name']
            my_activity=request.POST['activity']
            my_cardinality=request.POST['cardinality']
            new_booking = Booking()
            new_booking.activity = my_activity
            new_booking.cardinality = int(my_cardinality)
            new_booking.name = my_name
            new_booking.booking_date = datetime.strptime(my_date,'%d/%m/%Y %H:%M')
            new_booking.save()
            bookings = Booking.objects.all()

            return render(request,'home.html',{'today':today,'bookings':bookings,'messages':['prenotazione salvata']})
        except:
            err =  sys.exc_info()[0]
            print("Unexpected error:", sys.exc_info()[0])

            bookings = Booking.objects.all()
            return render(request,'home.html',{'today':today,'bookings':bookings,'errors':["{0}".format(err)]});
    return redirect('home')

def login(request):
    '''the login procedure'''
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        redirect('home')


def login(request):
    '''the logout procedure'''
    return render(request,'logout.html')
