import datetime
from datetime import date
from AvitoParser.config import DATES_dict


# this function return float time from string:
def str_to_time(time_string):
    time_datetime = datetime.datetime.strptime(time_string, "%H:%M").time()
    return round(float(time_datetime.hour) + float(time_datetime.minute) / 60, 2)


# this function accept int: year, int: month, int: day and return datetime object
def convert_to_datetime(year, month, day, time):
    date_string = f"{year}-{month}-{day} {int(time)}:{int((time - int(time)) * 60)}"
    date_object = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M")
    return date_object


# this function return date-time object from string pattern of avito:
def current_date(date_string_pattern):
    # get date:
    date_of_day = date_string_pattern[2:-8]
    time = date_string_pattern[-5:]
    if date_of_day == "сегодня":
        # today date/time:
        today_date = date.today()
        year, month, day = today_date.year, today_date.month, today_date.day
        time_float = str_to_time(time)

        return convert_to_datetime(year, month, day, time_float)

    elif date_of_day == "вчера":
        # yesterday date/time:
        today_date = date.today()
        yesterday_date = today_date - datetime.timedelta(days=1)
        yesterday_date.strftime('%Y-%m-%d')
        year, month, day = yesterday_date.year, yesterday_date.month, yesterday_date.day
        # str --> time-object:
        time_float = str_to_time(time)

        return convert_to_datetime(year, month, day, time_float)

    else:
        # get today year:
        current_year = datetime.datetime.now().year
        # get date number and month:
        date_list = date_of_day.split(' ')
        number = int(date_list[0])
        month = DATES_dict[date_list[1]]
        current_time = time.replace(':', '.')

        return convert_to_datetime(current_year, month, number, float(current_time))

