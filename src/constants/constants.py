from pymongo import MongoClient
import ssl

DB_URL = "mongodb://localhost:27017/store_monitoring?retryWrites=true&w=majority"
STORE_MONITORING_DB = "store_monitoring"

STORE_BUSINESS_TIME_COLLECTION = "store_business_time"
STORE_STATUS_COLLECTION = "store_status"
STORE_TIMEZONE_COLLECTION = "store_timezone"
STORE_REPORT_COLLECTION = "store_reports"

MONGO_CLIENT = MongoClient(DB_URL, ssl_cert_reqs=ssl.CERT_NONE)

MONGO_DB_CLIENT = MONGO_CLIENT[STORE_MONITORING_DB]