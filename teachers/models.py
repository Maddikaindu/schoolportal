from django.db import models
import uuid
from django.conf import settings
from students.models import Student
# Create your models here.
class Teacher(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    teacher_id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    name=models.CharField(max_length=30)
    subject_choices=(
        ('objectorientedprogramming','OOPS'),
        ('clanguage','CLANG'),
        ('computernetworks','CNS'),
        ('PYTHON','python')
    )
    subject=models.CharField(choices=subject_choices,max_length=30)
    def __str__(self):
       return self.user.username if self.user else self.name
class Marks(models.Model):
    student=models.ForeignKey('students.Student',on_delete=models.CASCADE,related_name='student_marks')
    subject_choices=(
        ('objectorientedprogramming','OOPS'),
        ('clanguage','CLANG'),
        ('computernetworks','CNS'),
        ('PYTHON','python')
    )
    subject=models.CharField(choices=subject_choices,max_length=30)
    marks=models.FloatField(blank=True,null=True)
    def __str__(self):
        return self.student.user.username if self.student.user else f"Stduent:{self.student.name}"