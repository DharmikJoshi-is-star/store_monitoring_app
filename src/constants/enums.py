
from enum import Enum

class StatusesEnum(Enum):
    STATUS_0 = (0, 'success', 'Report generated successfully', 'Complete')
    STATUS_1 = (1, 'processing', 'Report genetation in progress', 'Running')
    STATUS_2 = (2, 'invalid', 'invalid report id', 'invalid report id')
    STATUS_3 = (3, "failed", 'Something went wrong! while generating report please try again!', 'Something went wrong! while generating report please try again!')
    
    def __init__(self, code, status, status_msg, resp_msg):
        self.code = code
        self.status = status
        self.status_msg = status_msg
        self.resp_msg = resp_msg
    
    @property
    def get_code(self):
        return self.code

    @property
    def get_status(self):
        return self.status

    @property
    def get_status_msg(self):
        return self.status_msg

    @property
    def get_status_obj(self):
        return {
            'code': self.code,
            'status': self.status,
            'statusMsg': self.status_msg
        }
    
    @property
    def get_resp_obj(self):
        return {
            'report_status' : self.resp_msg
        }