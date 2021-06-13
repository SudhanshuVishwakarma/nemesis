from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# class Newuser(UserCreationForm):
#     email=forms.EmailField(required=True)
    
#     class Meta:
#         model = User
#         fields = ("username", "email", "password1", "password2", "address")
        
#     def save(self, commit=True):
#         user = super(Newuser, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user
        
def indexView(request):
    return render(request, 'index.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_url')
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/register.html',{'form':form})
    