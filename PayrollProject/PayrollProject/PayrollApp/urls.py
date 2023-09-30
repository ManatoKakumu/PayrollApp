from django.urls import path
from .views import (
    PayrollView, ShiftView, TeacherFormView,
    RegisterLessonView, ContactView, OutputCSVView,
    before_register_work_report, register_work_report,
)
from django.views.generic.base import TemplateView

app_name = "payroll_app"
urlpatterns = [
    path("", TemplateView.as_view(template_name="display/home.html"), name="home"),
    path("before_register_work_report/", before_register_work_report, name="before_register_work_report"),
    path("register_work_report/", register_work_report, name="register_work_report"),
    path("payroll/", PayrollView.as_view(), name="payroll"),
    path("shift/", ShiftView.as_view(), name="shift"),
    path("register_teacher/", TeacherFormView.as_view(), name="register_teacher"),
    path("register_lesson/", RegisterLessonView.as_view(), name="register_lesson"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("csv/", OutputCSVView.as_view(), name="csv"),
    path("success/", TemplateView.as_view(template_name="success.html"), name="success"),
]