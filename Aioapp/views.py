from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def buy(request):
    numbers = range(1, 4)
    context = {
        'numbers' : numbers
    }
    return render(request, 'buy.html', context)

def sell(request):

    return render(request, 'sell.html')

def message(request):

    return render(request, 'message.html')

def profile(request):

    return render(request, 'profile.html')

def first(request):

    return render(request, 'first.html')

def signup(request):

    return render(request, 'signup.html')

def login(request):

    return render(request, 'login.html')

def editprofile(request):

    return render(request, 'editprofile.html')

def viewbuy(request):

    return render(request, 'viewbuy.html')

def viewprofile(request):

    return render(request, 'viewprofile.html')

def popups(request):

    return render(request, 'popups.html')
