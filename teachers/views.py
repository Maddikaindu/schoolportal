from django.shortcuts import render,redirect
from . models import Student,Teacher
from . forms import MarksForm
from django.contrib  import messages
from django.shortcuts import get_object_or_404
from accounts.decorators import teacher_required

# Create your views here.
@teacher_required
def student_list(request):
    teacher=request.user.teacher
    students=Student.objects.filter(teacher=teacher)
    return render(request,'teacher_dashboard.html',{'students':students})

@teacher_required
def marks_create(request,student_id):
    student=get_object_or_404(Student,student_id=student_id)
    if request.method == 'POST':
        form=MarksForm(request.POST)
        if form.is_valid():
            marks=form.save(commit=False)
            marks.student=student
            marks.save()
            messages.success(request,'marks created successfully')
            return redirect('teacher_dashboard')
    else :
        form=MarksForm()
        return render(request,'marks_create.html',{'form':form,'student':student})
    





