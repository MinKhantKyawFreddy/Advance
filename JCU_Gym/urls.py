from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name="contact_success"),
    path('login/', views.login_view, name='login'),
    path("booking/", views.booking_view, name='booking'),
]