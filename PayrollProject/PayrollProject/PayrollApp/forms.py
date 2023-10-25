from django import forms
from .models import (
    Teachers, DayOfWeek, RegisterLesson, RegisterWorkReport,
    Payroll, Month, CSV, 
)
import datetime

# 講師情報登録Form
class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teachers
        fields = ["teacher_name", "fare"]

    # 講師名、交通費
    teacher_name = forms.CharField(max_length=20, label="講師名")
    fare = forms.IntegerField(label="交通費")


# 授業情報登録Form
class RegisterLessonForm(forms.ModelForm):

    class Meta:
        model = RegisterLesson
        exclude = ["day"]

    # 講師名
    teacher_name = forms.ModelChoiceField(queryset=Teachers.objects.all(), label="講師名")

    # 曜日、生徒名
    day_of_week = forms.ModelChoiceField(queryset=DayOfWeek.objects.all(), label="曜日")
    student1_1 = forms.CharField(max_length=20, label="生徒名1(15:15～16:45)", required=False)
    student1_2 = forms.CharField(max_length=20, label="生徒名2(15:15～16:45)", required=False)
    student2_1 = forms.CharField(max_length=20, label="生徒名1(16:50～18:20)", required=False)
    student2_2 = forms.CharField(max_length=20, label="生徒名2(16:50～18:20)", required=False)
    student3_1 = forms.CharField(max_length=20, label="生徒名1(18:25～19:55)", required=False)
    student3_2 = forms.CharField(max_length=20, label="生徒名2(18:25～19:55)", required=False)
    student4_1 = forms.CharField(max_length=20, label="生徒名1(20:00～21:30)", required=False)
    student4_2 = forms.CharField(max_length=20, label="生徒名2(20:00～21:30)", required=False)

    # 授業時間、PS2時間、高1,2年の回数、高3年の回数
    class_time = forms.FloatField(label="授業時間", required=False)
    PS2_time = forms.FloatField(label="PS2時間", required=False)
    high12_time = forms.FloatField(label="高校1,2年生の授業回数", required=False)
    high3_time = forms.FloatField(label="高校3年生の授業回数", required=False)

# 勤怠登録事前Form
class BeforeRegisterWorkReportForm(forms.ModelForm):

    class Meta:
        model = RegisterWorkReport
        fields = ["teacher_name", "day"]

    # 講師名
    teacher_name = forms.ModelChoiceField(queryset=Teachers.objects.all(), label="講師名")

    # 日付
    dt = datetime.datetime.today()
    dt = dt.date()
    day = forms.DateField(label="日付", initial=dt)

# 勤怠登録Form、RegisterLessonFormを継承
class RegisterWorkReportForm(RegisterLessonForm):

    class Meta:
        model = RegisterWorkReport
        exclude = ["day_of_week"]

    # 曜日の非表示化
    day_of_week = forms.CharField(widget=forms.HiddenInput(), required=False)

    # 日付
    day = forms.DateField(label="日付", required=False)

    # 事務給(単元テスト、テスト講評、その他)
    unit_test = forms.IntegerField(label="単元テスト回数", required=False)
    test_review = forms.IntegerField(label="テスト講評回数", required=False)
    others = forms.FloatField(label="その他の事務時間", required=False)

# 給与表示Form
class PayrollForm(forms.ModelForm):

    # 給与表示したい講師名と該当する月を選択
    teacher_name = forms.ModelChoiceField(queryset=Teachers.objects.all(), label="講師名")
    month = forms.ModelChoiceField(queryset=Month.objects.all(), label="月")

    class Meta:
        model = Payroll
        fields = "__all__"

# CSV出力Form
class CSVForm(forms.ModelForm):

    # CSV出力したい講師名と該当する月を選択
    teacher_name = forms.ModelChoiceField(queryset=Teachers.objects.all(), label="講師名")
    month = forms.ModelChoiceField(queryset=Month.objects.all(), label="月")

    class Meta:
        model = CSV
        fields = "__all__"