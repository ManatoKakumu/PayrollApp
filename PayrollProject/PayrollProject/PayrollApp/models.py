from django.db import models
import datetime

# Create your models here.

# 講師情報DB
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
    
# 曜日DB
class DayOfWeek(models.Model):
    day_id = models.IntegerField(primary_key=True)
    day_name = models.CharField(max_length=5)

    class Meta:
        db_table = "day_of_week"

    def __str__(self):
        return self.day_name

# 月DB
class Month(models.Model):
    month_id = models.IntegerField(primary_key=True)
    month = models.CharField(max_length=5)

    def __str__(self):
        return self.month
    
# 授業情報登録DB
class RegisterLesson(models.Model):

    class Meta:
        db_table = "lesson"

    teacher_name = models.CharField(null=False, max_length=20)

    # 授業報告(日付、生徒名、授業時間、PS2、高1,2年、高3年)
    day_of_week = models.CharField(null=False, max_length=5)
    student1_1 = models.CharField(null=True, max_length=20)
    student1_2 = models.CharField(null=True, max_length=20)
    student2_1 = models.CharField(null=True, max_length=20)
    student2_2 = models.CharField(null=True, max_length=20)
    student3_1 = models.CharField(null=True, max_length=20)
    student3_2 = models.CharField(null=True, max_length=20)
    student4_1 = models.CharField(null=True, max_length=20)
    student4_2 = models.CharField(null=True, max_length=20)

    class_time = models.FloatField(null=True)
    PS2_time = models.FloatField(null=True)
    high12_time = models.IntegerField(null=True)
    high3_time = models.IntegerField(null=True)

    def __str__(self):
        return "{} {}".format(self.teacher_name, self.day_of_week)
    
# 勤怠登録DB
class RegisterWorkReport(models.Model):

    class Meta:
        db_table = "work_report"

    teacher_name = models.CharField(null=False, max_length=20)

    dt = datetime.datetime.today()
    dt = dt.date()
    day = models.DateField(null=True)

    # 授業報告(日付、生徒名、授業時間、PS2、高1,2年、高3年)
    student1_1 = models.CharField(null=True, max_length=20)
    student1_2 = models.CharField(null=True, max_length=20)
    student2_1 = models.CharField(null=True, max_length=20)
    student2_2 = models.CharField(null=True, max_length=20)
    student3_1 = models.CharField(null=True, max_length=20)
    student3_2 = models.CharField(null=True, max_length=20)
    student4_1 = models.CharField(null=True, max_length=20)
    student4_2 = models.CharField(null=True, max_length=20)

    class_time = models.FloatField(null=True)
    PS2_time = models.FloatField(null=True)
    high12_time = models.IntegerField(null=True)
    high3_time = models.IntegerField(null=True)

     # 事務給(単元テスト、テスト講評、その他)
    unit_test = models.IntegerField(null=True)
    test_review = models.IntegerField(null=True)
    others = models.FloatField(null=True)

    def __str__(self):
        return "{} {}".format(self.teacher_name, self.day)