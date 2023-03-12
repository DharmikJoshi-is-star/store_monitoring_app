from src.daos import store_business_time_dao, store_report_dao, store_timezone_dao, store_status_dao
from src.constants.enums import StatusesEnum
from src.utils import util
import pandas as pd
import logging

logger = logging.getLogger("report_generator_service")

def __generate_all_store_report(store_report=None):
    report_status = None
    report_path = "/tmp/" + store_report["report_id"] + ".csv"
    logger.info("TESTTTTTT")
    all_store_ids = store_business_time_dao.all_store_ids()
    count = 0
    store_report_list = []
    try:
        for store_id in all_store_ids:
            logger.info("Process started!")
            # threading.Thread(target=find_last_hour_uptime_and_downtime_by_store_id,args=(store_id,), name=store_id).start()
            store_report_list.append(__generate_store_report(store_id))
            # generate_store_report("1000385412041408565")
            count += 1
            if (count == 5):
                break
        
        logger.info("Store Report generated successfully!")

        convert_dict_to_csv_file_save_path(store_report_list, report_path)
        report_status = StatusesEnum.STATUS_0.get_status
        store_report["report_path"] = report_path
    except Exception as e:
        logger.error("Exception occurred while generating the report file ", e)
        report_status = StatusesEnum.STATUS_3.get_status
    
    store_report_dao.update_report_status_report_path(store_report["report_id"], report_status, report_path)

    
    

def convert_dict_to_csv_file_save_path(list_dict, path):
    df = pd.DataFrame(list_dict)
    df.to_csv(path, index=False, header=True)


def __generate_store_report(store_id):

    store_report = {'store_id': store_id, 'uptime_last_hour': 'NA', 'uptime_last_day': 'NA',
                    'update_last_week': 'NA', 'downtime_last_hour': 'NA', 'downtime_last_day': 'NA', 'downtime_last_week': 'NA'}
    current_time = util.get_current_time_in_utc()
    last_hour = util.get_last_hour_in_utc()
    last_day = util.get_last_start_of_the_day()
    last_week = util.get_last_start_of_the_week()
    store_timezone_obj = store_timezone_dao.find_store_timezone_by_store_id(
        store_id)
    store_timezone_str = store_timezone_obj["timezone_str"] if store_timezone_obj is not None and "timezone_str" in store_timezone_obj else "America/Chicago"
    store_business_hours = list(
        store_business_time_dao.find_business_hours_by_store_id(store_id))
    store_status_list_last_hour = store_status_dao.find_store_status_by_store_id_and_start_end_time(
        store_id, last_hour, current_time)
    store_status_list_last_day = store_status_dao.find_store_status_by_store_id_and_start_end_time(
        store_id, last_day, current_time)
    store_status_list_last_week = store_status_dao.find_store_status_by_store_id_and_start_end_time(
        store_id, last_week, current_time)

    if (store_status_list_last_hour is not None):
        uptime, dowtime = __get_uptime_downtime_in_local_timezone_in_min(
            store_id, store_business_hours, store_status_list_last_hour, store_timezone_str)
        store_report['uptime_last_hour'] = uptime
        store_report['downtime_last_hour'] = dowtime

    if (store_status_list_last_day is not None):
        uptime, dowtime = __get_uptime_downtime_in_local_timezone_in_min(
            store_id, store_business_hours, store_status_list_last_day, store_timezone_str)
        store_report['uptime_last_day'] = uptime / 60
        store_report['downtime_last_day'] = dowtime / 60

    if (store_status_list_last_week is not None):
        uptime, dowtime = __get_uptime_downtime_in_local_timezone_in_min(
            store_id, store_business_hours, store_status_list_last_week, store_timezone_str)
        store_report['update_last_week'] = uptime / 60
        store_report['downtime_last_week'] = dowtime / 60

    return store_report


def __get_uptime_downtime_in_local_timezone_in_min(store_id, store_business_hours, store_status_list, store_timezone_str):
    effective_status_list = []
    count = 0
    for store_status in store_status_list:
        count += 1
        status_time = util.convert_utc_to_timezone(
            store_status["timestamp_utc"], store_timezone_str)
        business_hours = store_business_time_dao.get_business_hour_by_weekday(
            store_business_hours, status_time.weekday())

        for business_hour in business_hours:
            start_time, end_time = util.business_time_in_timezone(status_time.date(
            ), business_hour["start_time_local"], business_hour["end_time_local"], store_timezone_str)

            status_time = util.get_datetime_from_iso_format(str(status_time))
            start_time = util.get_datetime_from_iso_format(str(start_time))
            end_time = util.get_datetime_from_iso_format(str(end_time))

            if (start_time <= status_time and status_time <= end_time):
                effective_status_list.append(store_status)

    uptime = 0
    downtime = 0

    if (effective_status_list is not [] and len(effective_status_list) > 1):
        prev_store_status = effective_status_list[0]
        for i in range(1, len(effective_status_list)):
            time_diff = (util.convert_utc_to_timezone(effective_status_list[i]["timestamp_utc"], store_timezone_str) - util.convert_utc_to_timezone(
                prev_store_status["timestamp_utc"], store_timezone_str)).total_seconds() / 60
            if (prev_store_status["status"] == "active"):
                uptime += time_diff
            elif (prev_store_status["status"] == "inactive"):
                downtime += time_diff

            prev_store_status = effective_status_list[i]

    return uptime, downtime