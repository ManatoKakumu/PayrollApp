from django import forms
from .models import Teachers

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teachers
        fields = ["teacher_name"]

    