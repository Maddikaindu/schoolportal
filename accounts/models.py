from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    roles=(
        ('teacher','Teacher'),
        ('student','Student')
    )
    role=models.CharField(choices=roles,max_length=20,default='student')
    email_verified=models.BooleanField(default=False)
    email_token=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    
    def __str__(self):
        return f'{self.username}-{self.role}'
