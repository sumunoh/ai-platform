def validate_type(param_name,param_type,param_value):
    if param_value != None :
        if not isinstance(param_value, param_type):
            raise TypeError("{0} must be {1} but got {2}".format(param_name, param_type, type(param_value)))

def validate_mode(param_name, param_value, _mode):
    if param_value not in _mode:   
        raise ValueError("{0} must be one of {1}, but got {0} ='{2}'".format(param_name, _mode, param_value))
    
def validate_range(param_name,param_value,from_val,to_val):
    if param_value < from_val  or  param_value > to_val:
        raise ValueError("{0} is {1} {0} must be {2}~{3} but got {1}".format(param_name, param_value, from_val, to_val))
    
def validate_greater(param_name, param_value, from_val):
    if param_value <= from_val:
        raise ValueError("{0} is {1}, {0} must be greater than {2} but got {1}".format(param_name, param_value, from_val))
def validate_less(param_name, param_value, from_val):
    if param_value >= from_val:
            raise ValueError("{0} is {1}, {0} must be less than {2} but got {1}".format(param_name, param_value, from_val))
def validate_eq_n_greater(param_name, param_value, from_val):
    if param_value < from_val:
            raise ValueError("{0} is {1}, {0} must be equal or greater than {2} but got {1}".format(param_name, param_value, from_val))
def validate_eq_n_less(param_name, param_value, from_val):
    if param_value > from_val:
            raise ValueError("{0} is {1}, {0} must be equal or less than {2} but got {1}".format(param_name, param_value, from_val))
    