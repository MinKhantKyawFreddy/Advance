# your_app_name/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member # Import your Member model

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