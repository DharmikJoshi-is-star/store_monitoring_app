from src.daos import store_report_dao
from src.constants.enums import StatusesEnum
import threading
from src.services import report_generator_service
import base64

def generate_report(args):
    no_stores = args.get("no_stores", default=-1, type=int)
    report = store_report_dao.get_report_schema()
    store_report_dao.save(report=report)
    threading.Thread(target=report_generator_service.__generate_all_store_report, args=(
        report, no_stores, ), name=report["report_id"]).start()
    #report_generator_service.__generate_all_store_report(report)
    return {"report_id": report["report_id"]}


def get_report(report_id=None):
    resp = {}
    report = store_report_dao.get_report_by_id(report_id=report_id)

    if (report is None):
        raise Exception(StatusesEnum.STATUS_2.get_status_msg)

    if "status" in report:
        if report["status"] == StatusesEnum.STATUS_1.get_status:
            resp = StatusesEnum.STATUS_1.get_resp_obj
        elif report["status"] == StatusesEnum.STATUS_0.get_status:
            resp = StatusesEnum.STATUS_0.get_resp_obj
            resp["report_file"] = report["report_path"]
            with open(report["report_path"], 'rb') as binary_file:
                binary_file_data = binary_file.read()
                base64_encoded_data = base64.b64encode(binary_file_data)
                base64_message = base64_encoded_data.decode('utf-8')
                resp["report_file_in_base64"] = base64_message

    if resp == {}:
        raise Exception(StatusesEnum.STATUS_3.get_status_msg)

    return resp

