from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth import authenticate, login
from bookings.models import Booking
# Create your views here.

def home(request):
    '''the home request, should show app home page'''
    if request.method=='GET':
        today = datetime.now()
        bookings = Booking.objects.all()
        return render(request,'home.html',{'today':today,'bookings':bookings});
    if request.method =='POST':
        
        pass
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
