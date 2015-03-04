from django.shortcuts import render, redirect
from datetime import datetime,timedelta
from django.contrib.auth import authenticate, login
from bookings.models import Booking
import sys
# Create your views here.

def get_future_bookings():
    today = datetime.now()
    a_day = timedelta(1)
    yesterday = today - a_day
    yesterday = datetime(day=yesterday.day,month=yesterday.month,year=yesterday.year)
    return Booking.objects.filter(booking_date__gte=yesterday)

def home(request):
    '''the home request, should show app home page'''
    today = datetime.now()
    three_months = timedelta(90)
    forgetting_date = today-three_months
    to_delete = Booking.objects.filter(booking_date__lte=forgetting_date)
    for booking_to_delete in to_delete:
        booking_to_delete.delete()

    if request.method=='GET':
        bookings = get_future_bookings() #Booking.objects.all()
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
            bookings = get_future_bookings() #Booking.objects.all()

            return render(request,'home.html',{'today':today,'bookings':bookings,'messages':['prenotazione salvata']})
        except:
            err =  sys.exc_info()[0]
            print("Unexpected error:", sys.exc_info()[0])

            bookings = get_future_bookings() #Booking.objects.all()
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
