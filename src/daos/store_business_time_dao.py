
from src.constants.constants import MONGO_DB_CLIENT, STORE_BUSINESS_TIME_COLLECTION

STORE_BUSINESS_TIME = MONGO_DB_CLIENT[STORE_BUSINESS_TIME_COLLECTION]

def all_store_ids():
    return STORE_BUSINESS_TIME.distinct("store_id")

def get_business_hour_by_weekday(store_business_hours, day):
    business_hours = []
    for business_hour in store_business_hours:
        if business_hour["day"] == day:
            business_hours.append(business_hour)
    return business_hours

def find_business_hours_by_store_id(store_id):
    return STORE_BUSINESS_TIME.find({"store_id": store_id}).sort("day", 1)


