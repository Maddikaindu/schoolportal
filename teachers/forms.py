from django import forms
from . models import Teacher,Marks

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('name','subject')
class MarksForm(forms.ModelForm):
    class Meta:
        model=Marks
        fields=('subject','marks')