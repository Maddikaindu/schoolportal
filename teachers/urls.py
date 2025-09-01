from django.urls import path
from .import views


urlpatterns = [
    path('',views.student_list,name='teacher_dashboard'),
    path('create_marks/<uuid:student_id>',views.marks_create,name='marks_create')
]
