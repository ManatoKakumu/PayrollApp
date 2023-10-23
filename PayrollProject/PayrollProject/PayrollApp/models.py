from django.db import models
import datetime

# Create your models here.

# 講師情報DB
class Teachers(models.Model):

    # 講師id、講師名
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

    # 曜日id、曜日名
    day_id = models.IntegerField(primary_key=True)
    day_name = models.CharField(max_length=5)

    class Meta:
        db_table = "day_of_week"

    def __str__(self):
        return self.day_name

# 月DB
class Month(models.Model):

    # 月id、月名
    month_id = models.IntegerField(primary_key=True)
    month = models.CharField(max_length=5)

    class Meta:
        db_table = "month"

    def __str__(self):
        return self.month
    
# 授業情報ベースDB
class LessonBase(models.Model):
    
    # 講師名
    teacher_name = models.CharField(null=True, max_length=20)

    # 勤務日の日付
    dt = datetime.datetime.today()
    dt = dt.date()
    day = models.DateField(null=True)

    # 曜日、生徒名
    day_of_week = models.CharField(null=True, max_length=5)
    student1_1 = models.CharField(null=True, max_length=20)
    student1_2 = models.CharField(null=True, max_length=20)
    student2_1 = models.CharField(null=True, max_length=20)
    student2_2 = models.CharField(null=True, max_length=20)
    student3_1 = models.CharField(null=True, max_length=20)
    student3_2 = models.CharField(null=True, max_length=20)
    student4_1 = models.CharField(null=True, max_length=20)
    student4_2 = models.CharField(null=True, max_length=20)

    # 授業時間、PS2時間、高1,2年の回数、高3年の回数
    class_time = models.FloatField(null=True)
    PS2_time = models.FloatField(null=True)
    high12_time = models.IntegerField(null=True)
    high3_time = models.IntegerField(null=True)

    class Meta:
        db_table = "lesson_base"
        abstract = True


# 授業情報登録DB (LessonBaseを継承)
class RegisterLesson(LessonBase):

    class Meta:
        db_table = "lesson"

    def __str__(self):
        return "{} {}".format(self.teacher_name, self.day_of_week)
    
# 勤怠登録DB (LessonBaseを継承)
class RegisterWorkReport(LessonBase):

     # 事務給(単元テスト、テスト講評、その他)
    unit_test = models.IntegerField(null=True)
    test_review = models.IntegerField(null=True)
    others = models.FloatField(null=True)

    class Meta:
        db_table = "work_report"

    def __str__(self):
        return "{} {}".format(self.teacher_name, self.day)
    
# 給与表示DB
class Payroll(models.Model):

    class Meta:
        db_table ="payroll"

    teacher_name = models.CharField(max_length=20)
    month = models.CharField(max_length=5)