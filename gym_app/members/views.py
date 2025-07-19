from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Member
from django.contrib.auth.hashers import make_password, check_password

def register_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')

        try:
            hashed_password = make_password(password)
            member = Member.objects.create(firstname=full_name, email=email, password=hashed_password)
            messages.success(request, 'Account created successfully!')
            return redirect('login')
        except Exception as e:
            print("Error during registration:", e)
            messages.error(request, 'Account creation failed.')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            member = Member.objects.get(email=email)
            if check_password(password, member.password):
                messages.success(request, f"Welcome, {member.firstname}!")
                return redirect('home')
            else:
                messages.error(request, 'Incorrect password.')
        except Member.DoesNotExist:
            messages.error(request, 'Email not found.')
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def home_view(request):
    return render(request, 'home.html')
