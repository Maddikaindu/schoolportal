from django.db import models
from django.conf import settings
import uuid
# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
    student_id=models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
    teacher=models.ForeignKey('teachers.Teacher',on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=30)
    department_choices=(
        ('bca','BCA'),
        ('computerscience','CSE'),
        ('mechanical','ME'),
        ('civil','CV')
    )
    department=models.CharField(choices=department_choices,max_length=30)
    email=models.EmailField(null=True)

    def __str__(self):
            return self.user.username if self.user else f"Student: {self.name}"

        

        