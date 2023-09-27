from django.shortcuts import render
from django.views.generic.base import (
    View,
)
from . import forms
# Create your views here.

# ホーム画面
class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "home.html")


# 勤怠登録画面での処理
class AttendanceView(View):

    def get(self, request, *args, **kwargs):
        attendance_form = forms.TeacherForm()
        return render(request, "attendance.html", context={
            "attendance_form": attendance_form,
        })
    
    def post(self, request, *args, **kwargs):
        attendance_form = forms.TeacherForm(request.POST or None)
        if attendance_form.is_valid():
            attendance_form.save()
        return render(request, "attendance.html", context={
            "attendance_form": attendance_form,
        })