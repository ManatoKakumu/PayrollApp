from django.urls import path
from .views import (
    WorkReportView, PayrollView, ShiftView, TeacherFormView,
    RegisterClassView, ContactView, OutputCSVView,
)
from django.views.generic.base import TemplateView

app_name = "payroll_app"
urlpatterns = [
    path("", TemplateView.as_view(template_name="display/home.html"), name="home"),
    path("work_report/", WorkReportView.as_view(), name="work_report"),
    path("payroll/", PayrollView.as_view(), name="payroll"),
    path("shift/", ShiftView.as_view(), name="shift"),
    # path("register_teacher/", RegisterTeacherView.as_view(), name="register_teacher"),
    path("register_class/", RegisterClassView.as_view(), name="register_class"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("csv/", OutputCSVView.as_view(), name="csv"),
    path("success/", TemplateView.as_view(template_name="success.html"), name="success"),
    path("register_teacher/", TeacherFormView.as_view(), name="register_teacher"),
]