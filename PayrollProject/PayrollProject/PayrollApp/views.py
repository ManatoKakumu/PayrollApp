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

def calculate_payroll(lesson_fee, office_work_fee, class_time, 
                      PS2_time, high12_time, high3_time, 
                      unit_test, test_review, others):
    sum = 0

    if class_time is not None:
        class_time = class_time * lesson_fee
        sum += class_time
    
    if PS2_time is not None:
        PS2_time = PS2_time * 200
        sum += PS2_time
    
    if high12_time is not None:
        high12_time = high12_time * 200 * 1.5
        sum += high12_time
    
    if high3_time is not None:
        high3_time = high3_time * 300 * 1.5
        sum += high3_time
    
    if unit_test is not None:
        unit_test = unit_test * office_work_fee * 0.15
        sum += unit_test
    
    if test_review is not None:
        test_review = test_review * office_work_fee * 0.25
        sum += test_review
    
    if others is not None:
        others = others * office_work_fee
        sum += others

    return sum

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
    
    form = forms.RegisterWorkReportForm(initial=initial_values)
    
    if request.method == "POST":
        config = configparser.ConfigParser()
        config.read("config.ini", encoding="utf-8")
        lesson_fee = config.getint("salary_params", "lesson_fee")
        office_work_fee = config.getint("salary_params", "office_work_fee")
        form = forms.RegisterWorkReportForm(request.POST)

        if form.is_valid():

            class_time = form.cleaned_data["class_time"]
            PS2_time = form.cleaned_data["PS2_time"]
            high12_time = form.cleaned_data["high12_time"]
            high3_time = form.cleaned_data["high3_time"]
            unit_test = form.cleaned_data["unit_test"]
            test_review = form.cleaned_data["test_review"]
            others = form.cleaned_data["others"]
            new_day = form.cleaned_data["day"]
            new_teacher_name = form.cleaned_data["teacher_name"]
            
            today_payroll = calculate_payroll(lesson_fee, office_work_fee, class_time, 
                              PS2_time, high12_time, high3_time, 
                              unit_test, test_review, others)
            
            teacher_info = models.Teachers.objects.get(teacher_name=new_teacher_name)
            month = new_day.month

            if month == 1:
                teacher_info.Jan_salary += today_payroll
                teacher_info.save()
            elif month == 2:
                teacher_info.Feb_salary += today_payroll
                teacher_info.save()
            elif month == 3:
                teacher_info.Mar_salary += today_payroll
                teacher_info.save()
            elif month == 4:
                teacher_info.Apr_salary += today_payroll
                teacher_info.save()
            elif month == 5:
                teacher_info.May_salary += today_payroll
                teacher_info.save()
            elif month == 6:
                teacher_info.Jun_salary += today_payroll
                teacher_info.save()
            elif month == 7:
                teacher_info.Jul_salary += today_payroll
                teacher_info.save()
            elif month == 8:
                teacher_info.Aug_salary += today_payroll
                teacher_info.save()
            elif month == 9:
                teacher_info.Sep_salary += today_payroll
                teacher_info.save()
            elif month == 10:
                teacher_info.Oct_salary += today_payroll
                teacher_info.save()
            elif month == 11:
                teacher_info.Nov_salary += today_payroll
                teacher_info.save()
            elif month == 12:
                teacher_info.Dec_salary += today_payroll
                teacher_info.save()


            form.save()

            return redirect("payroll_app:success")
    
    form.fields['teacher_name'].initial = teacher_name
    form.fields['day'].initial = day
    ctx["form"] = form
    
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
