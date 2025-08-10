# your_app_name/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django import forms
from .models import Member, Booking  # Import your Member model
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # Get data from the form using the 'name' attributes from your HTML
        # These variable names (first_name, last_name, etc.) are fine for holding the data,
        # but the keyword arguments when creating the Member object must match the model.
        first_name_data = request.POST.get('first_name')
        last_name_data = request.POST.get('last_name')
        email_data = request.POST.get('email')
        phone_data = request.POST.get('phone')

        try:
            # Create a new Member object.
            # IMPORTANT: The keyword arguments here MUST EXACTLY MATCH
            # the field names (including capitalization) in your models.py
            member = Member(
                First_Name=first_name_data, # Matches models.py: First_Name
                Last_Name=last_name_data,   # Matches models.py: Last_Name
                Email=email_data,           # Matches models.py: Email
                Phone=phone_data            # Matches models.py: Phone
            )
            member.save()

            # Redirect to a success page after successful submission
            return redirect('contact_success')
        except Exception as e:
            # Catch any potential errors during model creation or saving
            # This is a general catch, for more specific errors, you'd use more specific exceptions.
            print(f"Error saving member: {e}")
            # You might want to add a message to the user here, e.g., using Django's messages framework
            # messages.error(request, 'There was an error submitting your form. Please try again.')
            return render(request, 'contact.html', {'error_message': 'There was an error processing your request.'})
    else:
        # If it's a GET request, just render the form
        return render(request, 'contact.html')

def contact_success(request):
    return render(request, 'submitted.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        try:
            username = User.objects.get(email=email).username
        except User.DoesNotExist:
            form.add_error('email', "No account with that email.")
        else:
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('password', "Incorrect password.")
    return render(request, 'home_app/login.html', {'form': form})


MAX_PER_SLOT = 5  # Example: Maximum bookings per time slot

def booking_view(request):
    message = None
    success = False
    
    if request.method == "POST":
        name = request.POST.get("first_name") + " " + request.POST.get("last_name")  # Combine first and last name
        time_slot = request.POST.get("time_slot")
        
        # Check if the time slot is full
        booking_count = Booking.objects.filter(time_slot=time_slot).count()
        if booking_count >= MAX_PER_SLOT:
            message = "Gym is full for that time"
        else:
            # Create or get the member
            member, created = Member.objects.get_or_create(name=name)
            # Create the booking
            Booking.objects.create(member=member, time_slot=time_slot)
            message = f"Booking confirmed for {name} at {time_slot}"
            success = True
        
        return render(request, 'booking.html', {'message': message, 'success': success})  # Changed to booking.html
    
    # For GET requests, render the empty form
    return render(request, 'booking.html', {'message': message, 'success': success})  # Changed to booking.html