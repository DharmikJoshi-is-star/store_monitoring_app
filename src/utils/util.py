from datetime import datetime, timedelta, time, timezone, date
import pytz

def get_current_time_in_utc():
    return datetime.today().astimezone(tz=timezone.utc) - timedelta(days=45)

def get_current_date():
    return date.today() - timedelta(days=45)

def get_last_hour_in_utc():
    return get_current_time_in_utc() - timedelta(hours=1)

def get_last_start_of_the_day():
    return datetime.combine(get_current_time_in_utc() - timedelta(days=1), time.min)

def get_last_start_of_the_week():
    return datetime.combine(get_current_time_in_utc() - timedelta(weeks=1), time.min)

def convert_utc_to_timezone(timestamp, timezone_str):
    timezone = pytz.timezone(timezone_str)
    return timezone.localize(timestamp).replace(microsecond=0)

def get_datetime_from_iso_format(datetime_str):
    return datetime.fromisoformat(datetime_str)

def business_time_in_timezone(date, start_time, end_time, store_timezone_str):
    start_date_time_str = str(date) + " " + start_time  # '18/09/19 01:55:19'
    end__date_time_str = str(date) + " " + end_time
    start_date_time = datetime.strptime(start_date_time_str, '%Y-%m-%d %H:%M:%S').replace(microsecond=0)
    end_date_time = datetime.strptime(end__date_time_str, '%Y-%m-%d %H:%M:%S').replace(microsecond=0)
    
    store_timezone = pytz.timezone(store_timezone_str)
    start_date_time = store_timezone.localize(start_date_time)
    end_date_time = store_timezone.localize(end_date_time)
    return start_date_time, end_date_time

def get_current_datetime():
    return datetime.now()