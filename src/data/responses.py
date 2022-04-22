
class ApiException(Exception):
    def __init__(self, code, error_message, result=None):
        self.result = result
        self.code = code
        self.error_message = error_message
        print(1)
#error message
OK = 'SUCCESS'
FALSE = 'FALSE'
