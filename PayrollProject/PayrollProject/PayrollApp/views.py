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
import configparser

# Create your views here.

def get_day_of_week(dt):
    day_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return (day_list[dt.weekday()])

def before_register_work_report(request):
    form = forms.BeforeRegisterWorkReportForm()
    
    if request.method == "POST":
        form = forms.BeforeRegisterWorkReportForm(request.POST)
        
        if form.is_valid():
            global teacher_name, day
            teacher_name = form.cleaned_data["teacher_name"]
            day = form.cleaned_data["day"]
            
            return redirect("payroll_app:register_work_report")
    
    return render(request, "display/before_work_report.html", context={
        "form": form,
    })

def register_work_report(request):
    ctx = {}
    day_of_week = get_day_of_week(day)
    lesson_info = models.RegisterLesson.objects.filter(teacher_name=teacher_name, day_of_week=day_of_week).values()
    day_month = day.month
    
    if lesson_info.exists():
        student1_1 = lesson_info[0]["student1_1"]
        student1_2 = lesson_info[0]["student1_2"]
        student2_1 = lesson_info[0]["student2_1"]
        student2_2 = lesson_info[0]["student2_2"]
        student3_1 = lesson_info[0]["student3_1"]
        student3_2 = lesson_info[0]["student3_2"]
        student4_1 = lesson_info[0]["student4_1"]
        student4_2 = lesson_info[0]["student4_2"]
        class_time = lesson_info[0]["class_time"]
        PS2_time = lesson_info[0]["PS2_time"]
        high12_time = lesson_info[0]["high12_time"]
        high3_time = lesson_info[0]["high3_time"]
        
        initial_values = {"teacher_name": teacher_name, "day":day, 
                          "student1_1": student1_1, "student1_2": student1_2, 
                          "student2_1": student2_1, "student2_2": student2_2, 
                          "student3_1": student3_1, "student3_2": student3_2, 
                          "student4_1": student4_1, "student4_2": student4_2, 
                          "class_time": class_time, "PS2_time": PS2_time, 
                          "high12_time": high12_time, "high3_time": high3_time, }
    else:
        initial_values = {"teacher_name": teacher_name, "day":day}
    
    form = forms.RegisterWorkReportForm(initial_values)
    ctx["form"] = form
    
    if request.method == "POST":
        config = configparser.ConfigParser()
        config.read("config.ini", encoding="utf-8")
        lesson_fee = config.getint("salary_params", "lesson_fee")
        office_work_fee = config.getint("salary_params", "office_work_fee")

        if form.is_valid():
            form.save()
            return redirect("payroll_app:success")
    
    return render(request, "display/work_report.html", ctx)


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
