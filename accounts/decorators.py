from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages

def teacher_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'teacher':
                return view_func(request, *args, **kwargs)
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('student_dashboard')  
        messages.error(request, 'You must login first.')
        return redirect('login_view')  
    return wrapper

def student_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.role == 'student':
                return view_func(request, *args, **kwargs)
            messages.error(request, 'You do not have permission to access this page.')
            return redirect('teacher_dashboard')  
        messages.error(request, 'You must login first.')
        return redirect('login_view')  
    return wrapper