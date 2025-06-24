from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User




class RegisterForm(UserCreationForm):
   
    
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password2']
        
      
    def save(self, commit = True):
        
        user = super().save(commit=False)
        if commit == True:
            user.save()
           
            
        return user
    
            
            
class User_Update_Form(forms.ModelForm):
    phone = forms.CharField(required= True)
    Image = forms.ImageField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name']
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            }) 
            
            
        if self.instance:
            
            try:
                user_profile = self.instance.profile
                self.fields['phone'].initial = user_profile.phone
            except Profile.DoesNotExist:
                user_profile = None
                
                
            try:
                user_image = self.instance.studentImage
                self.fields['Image'].initial = user_image.Image
            except Student_image.DoesNotExist:
                user_image = None
             

    def save(self, commit = True):
        user = super().save(commit=False)
        
        if commit:
            user.save()
            user_profile, _ = Profile.objects.get_or_create(user =user)                
            user_image, _ = Student_image.objects.get_or_create(user =user)                
            
            user_profile.phone = self.cleaned_data['phone']
            user_profile.save()
            
            user_image.Image = self.cleaned_data['Image']
            user_image.save()
            
        return user