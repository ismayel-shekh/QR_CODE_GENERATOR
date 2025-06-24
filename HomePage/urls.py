from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.Homepage, name='homepage'),
    path('user-detials/<int:pk>/', views.user_detail, name='user_detail'),
    path('all-user/', views.all_user, name='all_user'),
    path('add-user/', views.Add_user, name='adduser'),
    
]