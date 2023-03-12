
from src.constants.constants import MONGO_DB_CLIENT, STORE_TIMEZONE_COLLECTION

STORE_TIEMZONE = MONGO_DB_CLIENT[STORE_TIMEZONE_COLLECTION]

def find_store_timezone_by_store_id(store_id=None):
    return STORE_TIEMZONE.find_one({"store_id":store_id})
