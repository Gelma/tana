from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    '''the home request, should show app home page'''
    return render(request,'home.html');

def login(request):
    '''the login procedure'''
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        redirect('home')


def login(request):
    '''the login procedure'''
    return render(request,'logout.html')
