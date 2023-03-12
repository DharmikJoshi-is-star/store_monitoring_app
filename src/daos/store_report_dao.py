from src.constants.constants import MONGO_DB_CLIENT, STORE_REPORT_COLLECTION
from src.constants.enums import StatusesEnum
import uuid

STORE_REPORT = MONGO_DB_CLIENT[STORE_REPORT_COLLECTION]

def get_report_schema():
    return {
        "report_id" : str(uuid.uuid4()),
        "status": StatusesEnum.STATUS_1.get_status,
        "report_path": ""
    }

def save(report=None):
    if (report is not None):
        STORE_REPORT.save(report)

def get_report_by_id(report_id=None):
    if (report_id is not None and report_id is not ""):
        return STORE_REPORT.find_one(filter={"report_id": report_id})
    else:
        return None
    
def update_report_status_report_path(report_id=None, report_status=StatusesEnum.STATUS_1.get_status, report_path=""):
    if (report_id is not None and report_id is not ""):
        STORE_REPORT.update_one(filter={'report_id':report_id}, update={"$set":{"status": report_status, "report_path": report_path}})