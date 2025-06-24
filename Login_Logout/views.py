from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

from .forms import RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse



def Register(request):
    
    
    form = RegisterForm(request.POST or None)
 

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save()
          
            messages.success(request, 'Account registered successfully')
            return redirect('registerpage')
        
        else:
            form.save()
            messages.error(request, 'Registration failed. Please correct the errors.')
    
    return render(request, 'register.html', {'form': form})
    






def User_login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(email = email, password = password)
            
            if user is not None:
                login(request,user)
                messages.success(request, f' welcome {user.first_name} {user.last_name} !!')
                return redirect('all_user')
            
            else:
                messages.success(request,'Loggin info incorrect')
                
    else:
        form = AuthenticationForm()
        
    return render(request,'login.html', {'form':form} )




@login_required
def LogoutView(request):
    user = request.user
    logout(request)
    messages.success(request, f'{user.first_name} {user.last_name} is successfully logged out.')
    return redirect('loginpage')
 
