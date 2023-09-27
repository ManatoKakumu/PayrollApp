from django.db import models

# Create your models here.

class Teachers(models.Model):
    teacher_name = models.CharField(max_length=20)

    class Meta:
        db_table = "teachers"