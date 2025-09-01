from django.shortcuts import render,redirect
from . models import Student
from teachers.models import Marks
from . forms import StudentForm
from teachers.forms import MarksForm
from django.contrib  import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.decorators import teacher_required,student_required

# Create your views here.
@login_required
@teacher_required
def student_create(request):
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'student created successfully')
            return redirect('teacher_dashboard')
        
    else :
        form=StudentForm()
        return render(request,'student_create.html',{'form':form})
    
@login_required        
@teacher_required
def student_update(request,student_id):
    student=get_object_or_404(Student,student_id=student_id)
    marks_all=student.student_marks.all()
    if request.method == 'POST':
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            for mark in marks_all:
                marks_value=request.POST.get(str(mark.id))
                if marks_value:
                    mark.marks=marks_value
                    mark.save()
            messages.info(request,'student updated successfully')
            return redirect('teacher_dashboard')
        
    else:
        form=StudentForm(instance=student)
        return render(request,'student_update.html',{'form':form,'student':student,'marks_all':marks_all})
    
@login_required  
@teacher_required
def student_delete(request,student_id):
    student=get_object_or_404(Student,student_id=student_id)
    student.delete()
    messages.info(request,'student deleted successfully')
    return redirect('teacher_dashboard')

@login_required
@student_required
def student_dashboard(request):
    student=get_object_or_404(Student,user=request.user)
    marks=Marks.objects.filter(student=student)
    return render(request,'student_dashboard.html',{'student':student,'marks':marks})
