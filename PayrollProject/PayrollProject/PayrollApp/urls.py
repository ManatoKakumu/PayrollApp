from django.urls import path
from .views import (
    WorkReportView, PayrollView, ShiftView, TeacherFormView,
    RegisterLessonView, ContactView, OutputCSVView,
    test1, test2,
)
from django.views.generic.base import TemplateView

app_name = "payroll_app"
urlpatterns = [
    path("", TemplateView.as_view(template_name="display/home.html"), name="home"),
    path("work_report/", WorkReportView.as_view(), name="work_report"),
    path("payroll/", PayrollView.as_view(), name="payroll"),
    path("shift/", ShiftView.as_view(), name="shift"),
    path("register_teacher/", TeacherFormView.as_view(), name="register_teacher"),
    path("register_lesson/", RegisterLessonView.as_view(), name="register_lesson"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("csv/", OutputCSVView.as_view(), name="csv"),
    path("success/", TemplateView.as_view(template_name="success.html"), name="success"),
    path("test1/", test1, name="test1"),
    path("test2/", test2, name="test2"),
]