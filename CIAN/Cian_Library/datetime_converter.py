import datetime
from CIAN.CianParser.config import MONTH_DICT


def current_date(date_arr):
    today = datetime.datetime.now()
    year = today.year
    date_arr = [str(year)] + date_arr
    try:
        date_arr[2] = MONTH_DICT[date_arr[2]]
        date_string = ' '.join(date_arr)
        date_object = datetime.datetime.strptime(date_string, '%Y %d %b')
        if today < date_object:
            date_object -= datetime.timedelta(days=365)

        return date_object

    except Exception as _ex:
        print(f"[WARNING] : {_ex}")
        return datetime.datetime.now()

