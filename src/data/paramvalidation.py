from responses import ApiException

def validate_type(param_name,param_type,param_value):
    if param_value != None :
        if not isinstance(param_value, param_type):
            code = 400
            error_message = "TypeError : {0} must be {1} but got {2}".format(param_name, param_type, type(param_value))
            result = 0
            raise TypeError("{0} must be {1} but got {2}".format(param_name, param_type, type(param_value)))

def validate_range(param_name,param_value,from_val,to_val):
    if not [from_val > param_value and param_value > to_val]:
            code = 400
            error_message = "ValueError : {0} is {1} {0} must be {2}~{3} but got {1}".format(param_name, param_value, from_val, to_val)
            result = 0        
            raise ValueError("{0} is {1} {0} must be {2}~{3} but got {1}".format(param_name, param_value, from_val, to_val))

def validate_mode(param_name, param_value, _mode):
    if param_value not in _mode:   
        code = 400
        error_message = "ValueError : {0} must be one of {1}, but got activation='{2}'".format(param_name, _mode, param_value)
        result = 0            

        raise ValueError("{0} must be one of {1}, but got activation='{2}'".format(param_name, _mode, param_value))