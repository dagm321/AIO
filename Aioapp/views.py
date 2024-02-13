from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        if (password != re_password):
            raise ValueError("Your password must much")


        user = User.objects.create_user(
            full_name = full_name,
            phone_number = phone_number,
            username = username,
            password = password
        )
        messages.success(request, "Successfully reqistered")
        return redirect('login')

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

# @login_required
def buy(request):
    numbers = range(1, 4)
    products = Product.objects.order_by('-date')
    context = {
        'numbers' : numbers,
        'products' : products
    }
    return render(request, 'buy.html', context)

# @login_required
def sell(request):
    if request.method == 'POST':
        product_title = request.POST.get('product_title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        price = request.POST.get('price')
        new_checkbox = request.POST.get('new_checkbox')
        used_checkbox = request.POST.get('used_checkbox')

        if not product_title:
            raise Exception("Error: Please provide product title")

        if not description:
            raise Exception("Error: Please provide description")

        if not price:
            raise Exception("Error: please provide a price")
        if not (used_checkbox or new_checkbox):
            raise Exception("Error: Please provide a product status")
        
        if not image:
            raise Exception("Error: please provide an image")

        if not request.user.is_authenticated:
            raise PermissionError("Please login first")
        
        product = Product(
            product_title = product_title,
            description = description,
            image = image,
            price = price,
            user = request.user,
            status = "Used" if used_checkbox else "New" if new_checkbox else ""
        )   
        product.save()
        messages.success(request, "Product Posted Successfully") 

    return render(request, 'sell.html')
# @login_required
def message(request):

    return render(request, 'message.html')

# @login_required
def profile(request):
    user = request.user
    context = {
        'user' : user
    }
    return render(request, 'profile.html', context)

def first(request):

    return render(request, 'first.html')


# @login_required
def editprofile(request):
    user = request.user
    if request.method == 'POST':
        user.full_name = request.POST.get('full_name')
        user.username = request.POST.get('username')
        user.description = request.POST.get('description')
        new_phone_number = request.POST.get('phone_number')
        user.password = request.POST.get('password')
        re_password = request.POST.get('re_password')
        image = request.FILES.get('image')
        user.profile_picture = image
        # user.set_password(password)
        if (user.phone_number == new_phone_number):
            user.phone_number = new_phone_number
        elif (new_phone_number != get_user_model().objects.filter(phone_number=new_phone_number)):
            user.phone_number = new_phone_number
        else :
            raise Exception("phone number must be unique")
        user.save()

        
        # Update the session to avoid automatic logout after password change
        update_session_auth_hash(request, user)
        messages.success(request, "Profile Saved")
        return redirect('profile')


    context = {
        'user' : user
    }
    return render(request, 'editprofile.html', context)
# @login_required
def viewbuy(request):

    return render(request, 'viewbuy.html')
# @login_required
def viewprofile(request):

    return render(request, 'viewprofile.html')
# @login_required
def popups(request):

    return render(request, 'popups.html')


def custom_logout(request):
    logout(request)
    return redirect('login')
