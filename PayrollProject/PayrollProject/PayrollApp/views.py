from django.shortcuts import render, redirect
from django.views.generic.base import (
    View, 
)
from django.views.generic.edit import (
    FormView,
)
from . import forms
from . import models
from django.urls import reverse_lazy
from django.contrib.sessions.models import Session
# Create your views here.

# 勤務報告画面
class WorkReportView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "display/work_report.html")
    
    def post(self, request, *args, **kwargs):
        pass

# 給与計算画面
class PayrollView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "display/payroll.html")
    
    def post(self, request, *args, **kwargs):
        pass

# シフト画面
class ShiftView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "display/shift.html")
    
    def post(self, request, *args, **kwargs):
        pass

# 講師情報登録Form
class TeacherFormView(FormView):

    template_name = "registration/teacher.html"
    form_class = forms.TeacherForm
    success_url = reverse_lazy("payroll_app:success")

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(TeacherFormView, self).form_valid(form)


# 授業情報登録画面
class RegisterLessonView(FormView):

    template_name = "registration/lesson.html"
    form_class = forms.RegisterLessonForm
    success_url = reverse_lazy("payroll_app:success")

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(RegisterLessonView, self).form_valid(form)

    
# 連絡発信画面
class ContactView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "registration/contact.html")
    
    def post(self, request, *args, **kwargs):
        pass

# csv出力画面
class OutputCSVView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "registration/csv.html")
    
    def post(self, request, *args, **kwargs):
        pass
