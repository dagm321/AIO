from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth import get_user_model

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        user = User.objects.create_user(
            full_name = full_name,
            phone_number = phone_number,
            username = username,
            password = password
        )

    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('buy')
    return render(request, 'login.html')

def buy(request):
    numbers = range(1, 4)
    products = Product.objects.all()
    context = {
        'numbers' : numbers,
        'products' : products
    }
    return render(request, 'buy.html', context)

def sell(request):
    if request.method == 'POST':
        product_title = request.POST.get('product_title')
        description = request.POST.get('description')
        image = request.POST.get('image')
        price = request.POST.get('price')
        new_checkbox = request.POST.get('new_checkbox')
        used_checkbox = request.POST.get('used_checkbox')

        product = Product(
            product_title = product_title,
            description = description,
            image = image,
            price = price,
            username = request.user
        )   
        product.save()

    return render(request, 'sell.html')

def message(request):

    return render(request, 'message.html')

def profile(request):

    return render(request, 'profile.html')

def first(request):

    return render(request, 'first.html')



def editprofile(request):

    return render(request, 'editprofile.html')

def viewbuy(request):

    return render(request, 'viewbuy.html')

def viewprofile(request):

    return render(request, 'viewprofile.html')

def popups(request):

    return render(request, 'popups.html')
