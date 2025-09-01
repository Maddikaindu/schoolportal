from django.urls import path
from .import views


urlpatterns = [
    path('dashboard/',views.student_dashboard,name='student_dashboard'),
    path('create_student/',views.student_create,name='student_create'),
    path('update_student/<uuid:student_id>/',views.student_update,name='student_update'),
    path('create_student/<uuid:student_id>/',views.student_delete,name='student_delete')
]
