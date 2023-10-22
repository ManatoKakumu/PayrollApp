from django.urls import path
from .views import (
    ShiftView, TeacherFormView,
    RegisterLessonView, ContactView, OutputCSVView,
    BeforeRegisterWorkReportView, RegisterWorkReportView,
    PayrollView, ResultPayrollView, 
)
from django.views.generic.base import TemplateView

app_name = "payroll_app"
urlpatterns = [
    path("", TemplateView.as_view(template_name="display/home.html"), name="home"),
    path("before_register_work_report/", BeforeRegisterWorkReportView.as_view(), name="before_register_work_report"),
    path("register_work_report/", RegisterWorkReportView.as_view(), name="register_work_report"),
    path("payroll/", PayrollView.as_view(), name="payroll"),
    path("payroll_result/", ResultPayrollView.as_view(), name="payroll_result"),
    path("shift/", ShiftView.as_view(), name="shift"),
    path("register_teacher/", TeacherFormView.as_view(), name="register_teacher"),
    path("register_lesson/", RegisterLessonView.as_view(), name="register_lesson"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("csv/", OutputCSVView.as_view(), name="csv"),
    path("success/", TemplateView.as_view(template_name="success.html"), name="success"),
]