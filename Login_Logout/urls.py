from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
   path('Register/', views.Register, name='registerpage'),
   path('Login/', views.User_login, name='loginpage'),
   path('Logout/', views.LogoutView, name='LogoutViewpage'),
    
]