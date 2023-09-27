import datetime

day = datetime.datetime.today()
day = day.date()
print(day)

def get_day_of_week(dt):
    day_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    return(day_list[dt.weekday()])

week_of_day = get_day_of_week(day)
print(week_of_day)