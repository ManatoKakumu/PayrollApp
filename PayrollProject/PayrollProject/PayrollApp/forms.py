from django import forms
from .models import (
    Teachers, DayOfWeek, RegisterLesson, 
)
import datetime

# 講師情報登録Form
class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teachers
        fields = ["teacher_name", "fare"]

    teacher_name = forms.CharField(max_length=20, label="講師名")
    fare = forms.IntegerField(label="交通費")


# 授業情報登録Form
class RegisterLessonForm(forms.ModelForm):

    class Meta:
        model = RegisterLesson
        fields = "__all__"

    teacher_name = forms.ModelChoiceField(queryset=Teachers.objects.all(), label="講師名")

    # 授業報告(日付、生徒名、授業時間、PS2、高1,2年、高3年)
    day_of_week = forms.ModelChoiceField(queryset=DayOfWeek.objects.all(), label="曜日")
    student1_1 = forms.CharField(max_length=20, label="生徒名1(15:15～16:45)", required=False)
    student1_2 = forms.CharField(max_length=20, label="生徒名2(15:15～16:45)", required=False)
    student2_1 = forms.CharField(max_length=20, label="生徒名1(16:50～18:20)", required=False)
    student2_2 = forms.CharField(max_length=20, label="生徒名2(16:50～18:20)", required=False)
    student3_1 = forms.CharField(max_length=20, label="生徒名1(18:25～19:55)", required=False)
    student3_2 = forms.CharField(max_length=20, label="生徒名2(18:25～19:55)", required=False)
    student4_1 = forms.CharField(max_length=20, label="生徒名1(20:00～21:30)", required=False)
    student4_2 = forms.CharField(max_length=20, label="生徒名2(20:00～21:30)", required=False)

    class_time = forms.FloatField(label="授業時間", required=False)
    PS2_time = forms.FloatField(label="PS2時間", required=False)
    high12_time = forms.FloatField(label="高校1,2年生の授業回数", required=False)
    high3_time = forms.FloatField(label="高校3年生の授業回数", required=False)