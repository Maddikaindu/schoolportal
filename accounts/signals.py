from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
from students.models import Student
from teachers.models import Teacher

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser or instance.is_staff:
            return  

        if instance.role == 'student':
            Student.objects.create(user=instance, name=instance.username)
        elif instance.role == 'teacher':
            Teacher.objects.create(user=instance, name=instance.username)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.is_superuser or instance.is_staff:
        return  

    if instance.role == 'student' and hasattr(instance, 'student'):
        instance.student.save()
    elif instance.role == 'teacher' and hasattr(instance, 'teacher'):
        instance.teacher.save()