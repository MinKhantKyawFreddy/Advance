from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]