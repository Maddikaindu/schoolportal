from django.shortcuts import render,redirect
from .models import CustomUser
from .forms import CustomUserRegistrationForm,LoginForm
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form=CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.email_verified =True
            user.save()
            messages.success(request,f'{user.role} registered successfully')
            return redirect('login')
    else:
       form=CustomUserRegistrationForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'student':
                    return redirect('student_dashboard')
                elif user.role == 'teacher':
                    return redirect('teacher_dashboard')
            else:
                messages.error(request, 'Please verify your email before logging in.')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html',{'form':form})

def logout_view(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('login')