
from src.constants.constants import MONGO_DB_CLIENT, STORE_STATUS_COLLECTION

STORE_STATUS = MONGO_DB_CLIENT[STORE_STATUS_COLLECTION]

def find_store_status_by_store_id_and_start_end_time(store_id, start_time, end_time):
    return STORE_STATUS.find({"store_id": store_id, "timestamp_utc":{"$gte": start_time,"$lte": end_time} }).sort("timestamp_utc", 1)
