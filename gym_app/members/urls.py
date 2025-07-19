from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'),  # Root path named 'register'
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),  # Added home URL
]