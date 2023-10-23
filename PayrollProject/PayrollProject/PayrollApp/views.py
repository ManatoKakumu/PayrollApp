from django.shortcuts import render, redirect
from django.views.generic.base import (
    View, 
)
from django.views.generic.edit import (
    FormView,
)
from . models import (
    RegisterLesson, Teachers, 
)
from . forms import (
    BeforeRegisterWorkReportForm, RegisterWorkReportForm, PayrollForm, 
    TeacherForm, RegisterLessonForm, 
)
from django.urls import reverse_lazy
import configparser

# Create your views here.

# 講師名と該当する日付の選択画面
class BeforeRegisterWorkReportView(View):
    
    def get(self, request):
        form = BeforeRegisterWorkReportForm()
        return render(request, "display/before_work_report.html", context={
            "form": form,
        })
    
    def post(self, request):
        form = BeforeRegisterWorkReportForm(request.POST)
        
        if form.is_valid():
            global teacher_name, day
            teacher_name = form.cleaned_data["teacher_name"]
            day = form.cleaned_data["day"]
            return redirect("payroll_app:register_work_report")
        
        return render(request, "display/before_work_report.html", context={
            "form": form,
        })

# 勤務報告
class RegisterWorkReportView(View):

    # 日付から曜日取得
    def get_day_of_week(self, dt):
        day_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
        return (day_list[dt.weekday()])
    
    # 給与計算処理
    def calculate_payroll(self,lesson_fee=0, office_work_fee=0, 
                      class_time=0, PS2_time=0, high12_time=0, high3_time=0, 
                      unit_test=0, test_review=0, others=0):
        sum = 0

        def calculate_individual(item, val):
            if item is not None:
                return item * val
            return 0

        sum += calculate_individual(class_time, lesson_fee)
        sum += calculate_individual(PS2_time, 200)
        sum += calculate_individual(high12_time, 200 * 1.5)
        sum += calculate_individual(high3_time, 300 * 1.5)
        sum += calculate_individual(unit_test, office_work_fee * 0.15)
        sum += calculate_individual(test_review, office_work_fee * 0.25)
        sum += calculate_individual(others, office_work_fee)

        return sum
    
    def get(self, request):
        self.ctx = {}
        day_of_week = self.get_day_of_week(day)
        lesson_info = RegisterLesson.objects.filter(teacher_name=teacher_name, day_of_week=day_of_week).first()
        
        if lesson_info:
            field_names = ["student1_1", "student1_2", "student2_1", "student2_2", 
                           "student3_1", "student3_2", "student4_1", "student4_2", 
                           "class_time", "PS2_time", "high12_time", "high3_time"]
            initial_values = {field: lesson_info.__dict__[field] for field in field_names}
            initial_values.update({"teacher_name": teacher_name, "day": day})
        else:
            initial_values = {"teacher_name": teacher_name, "day": day}
        
        form = RegisterWorkReportForm(initial=initial_values)
        self.ctx["form"] = form
        return render(request, "display/work_report.html", self.ctx)
    
    def post(self, request):
        config = configparser.ConfigParser()
        config.read("config.ini", encoding="utf-8")
        lesson_fee = config.getint("salary_params", "lesson_fee")
        office_work_fee = config.getint("salary_params", "office_work_fee")
        
        form = RegisterWorkReportForm(request.POST)
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
            
            today_payroll = self.calculate_payroll(lesson_fee, office_work_fee, class_time, 
                                              PS2_time, high12_time, high3_time, 
                                              unit_test, test_review, others)
            
            teacher_info = Teachers.objects.get(teacher_name=new_teacher_name)
            today_payroll += teacher_info.fare
            month = new_day.month
            
            month_fields = {
                1: "Jan_salary", 2: "Feb_salary", 3: "Mar_salary", 4: "Apr_salary",
                5: "May_salary", 6: "Jun_salary", 7: "Jul_salary", 8: "Aug_salary",
                9: "Sep_salary", 10: "Oct_salary", 11: "Nov_salary", 12: "Dec_salary",
            }
            
            if month in month_fields:
                field_name = month_fields[month]
                setattr(teacher_info, field_name, getattr(teacher_info, field_name) + today_payroll)
                teacher_info.save()
            
            form.save()
            return redirect("payroll_app:success")
        
        return render(request, "display/work_report.html", self.ctx)


# 給与選択画面 (給与表示する講師名と該当する月を選ぶ)
class PayrollView(View):
    
    def get(self, request):
        form = PayrollForm()

        return render(request, "display/payroll.html", context={
            "form": form,
        })

    def post(self, request):
        form = PayrollForm(request.POST)

        if form.is_valid():
            # 入力された講師名と該当する月をセッションに保存する処理
            teacher_name_for_payroll = form.cleaned_data["teacher_name"]
            month_for_payroll = str(form.cleaned_data["month"])

            teacher = Teachers.objects.get(teacher_name=teacher_name_for_payroll)
            
            request.session['teacher_id_for_payroll'] = teacher.teacher_id
            request.session['month_for_payroll'] = month_for_payroll

            return redirect("payroll_app:payroll_result")

        return render(request, "display/payroll.html", context={
            "form": form,
        })

# 給与表示画面 (PayrollViewにて選択したものに該当する給料を表示する)
class ResultPayrollView(View):

    def get(self, request):
        teacher_id_for_payroll = request.session.get('teacher_id_for_payroll')
        month_for_payroll = request.session.get('month_for_payroll')

        # セッション情報がなければ、給与表示する講師名と該当する月を選ぶ画面に戻る
        if teacher_id_for_payroll is None or month_for_payroll is None:
            return redirect("payroll_app:payroll")

        try:
            teacher = Teachers.objects.get(pk=teacher_id_for_payroll)
        except Teachers.DoesNotExist:
            teacher = None

        if teacher is None:
            return redirect("payroll_app:payroll")

        month_salary_mapping = {
            "1月": "Jan_salary", "2月": "Feb_salary", "3月": "Mar_salary", "4月": "Apr_salary", 
            "5月": "May_salary", "6月": "Jun_salary", "7月": "Jul_salary", "8月": "Aug_salary",
            "9月": "Sep_salary", "10月": "Oct_salary", "11月": "Nov_salary", "12月": "Dec_salary",
        }
        salary = getattr(teacher, month_salary_mapping.get(month_for_payroll))

        # 給与が0円かそれ以外かで表示する画面を分ける
        if salary == 0:
            return render(request, "display/payroll_none_data.html", context={
                "month": month_for_payroll,
            })

        return render(request, "display/payroll_show.html", context={
            "salary": salary, "month": month_for_payroll,
        })

# 講師情報登録画面
class TeacherFormView(FormView):

    template_name = "registration/teacher.html"
    form_class = TeacherForm
    success_url = reverse_lazy("payroll_app:success")

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(TeacherFormView, self).form_valid(form)


# 授業情報登録画面
class RegisterLessonView(FormView):

    template_name = "registration/lesson.html"
    form_class = RegisterLessonForm
    success_url = reverse_lazy("payroll_app:success")

    def form_valid(self, form):
        if form.is_valid():
            form.save()
        return super(RegisterLessonView, self).form_valid(form)
