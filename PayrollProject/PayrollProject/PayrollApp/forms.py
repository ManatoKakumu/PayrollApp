from django import forms
from .models import (
    Teachers,
)
import datetime

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teachers
        fields = ["teacher_name", "fare"]

    teacher_name = forms.CharField(max_length=20, label="講師名")
    fare = forms.IntegerField(label="交通費", initial=0)