from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        first_name_data = request.POST.get('first_name')
        last_name_data = request.POST.get('last_name')
        email_data = request.POST.get('email')
        phone_data = request.POST.get('phone')

        try:
            member = Member(
                first_name=first_name_data,
                last_name=last_name_data,
                email=email_data,
                phone=phone_data
            )
            member.save()
            return redirect('contact_success')
        except Exception as e:
            print(f"Error saving member: {e}")
            return render(request, 'contact.html', {'error_message': 'There was an error processing your request.'})
    else:
        return render(request, 'contact.html')

def contact_success(request):
    return render(request, 'submitted.html')