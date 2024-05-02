from src.logger import logging
import sys
def error_message_details(error,error_detail : sys):
    _,__,exe_tb = error_detail.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    line_no = exe_tb.tb_lineno
    error_message = 'Error in python script name [{0}] in line [{1}], exrror message [{2}]'.format(
        file_name,
        line_no,
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail = error_detail)

    def __str__(self):
        return self.error_message

if __name__ == '__main__':

    try:
        a = 1/0
    except Exception as e:
        logging.info('div 0 error')
        raise CustomException(e,sys)