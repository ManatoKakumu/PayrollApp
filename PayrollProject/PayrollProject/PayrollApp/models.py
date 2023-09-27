from django.db import models

# Create your models here.

class Teachers(models.Model):
    teacher_id = models.IntegerField(primary_key=True)
    teacher_name = models.CharField(max_length=20)

    # 交通費
    fare = models.IntegerField()
    
    # 各月の給与
    Jan_salary = models.FloatField(default=0)
    Feb_salary = models.FloatField(default=0)
    Mar_salary = models.FloatField(default=0)
    Apr_salary = models.FloatField(default=0)
    May_salary = models.FloatField(default=0)
    Jun_salary = models.FloatField(default=0)
    Jul_salary = models.FloatField(default=0)
    Aug_salary = models.FloatField(default=0)
    Sep_salary = models.FloatField(default=0)
    Oct_salary = models.FloatField(default=0)
    Nov_salary = models.FloatField(default=0)
    Dec_salary = models.FloatField(default=0)

    class Meta:
        db_table = "teachers"

    def __str__(self):
        return self.teacher_name