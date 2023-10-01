from django.contrib import admin
from .models import Teachers, DayOfWeek, RegisterLesson, RegisterWorkReport


# Register your models here.

admin.site.register(Teachers)
admin.site.register(RegisterLesson)
admin.site.register(DayOfWeek)
admin.site.register(RegisterWorkReport)