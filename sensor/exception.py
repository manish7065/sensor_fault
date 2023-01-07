
import sys,os
from sensor.logger import logging


def error_message_detail(error_message:Exception, error_detail: sys)->str:
    _, _, exec_tb = error_detail.exc_info()
    exception_block_line_number = exec_tb.tb_frame.f_lineno
    try_block_line_number = exec_tb.tb_lineno
    file_name = exec_tb.tb_frame.f_code.co_filename

    error_message = f"""
        Error occured in script: 
        [ {file_name} ] at 
        try block line number: [{try_block_line_number}] and exception block line number: [{exception_block_line_number}] 
        error message: [{error_message}]
        """
    return error_message

class SensorException(Exception):
    def __init__(self,error_message:Exception,error_detail:sys):
        """
        :para :error_message in string,
                error_details from system(sys)
        
        """
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message, error_detail=error_detail)
        logging.info(self.error_message)

    def __str__(self):
        return self.error_message 