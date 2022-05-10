import re
def validate_type(name: str, param, param_type, exception = 'general'):
    if name is None:
        raise TypeError("name parameter is None")
    if param is None:
        raise TypeError("param parameter is None")
    if param_type is None:
        raise TypeError("param_type parameter is None")

    if not isinstance(param, param_type):
        raise TypeError("{0} type must be {1} but got {2} type".format(name, param_type, type(param)))
    
    if exception == 'ip':
        p = '^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$'
        ip_valid = re.search(p, param)
        if ip_valid is None:
            raise TypeError("ip regular expression is xxx.xxx.xxx.xxx")
    else:
        pass    


def validate_greater(name: str, param, value):
    if name is None:
        raise TypeError("name parameter is None")
    if param is None:
        raise TypeError("param parameter is None")
    if value is None:
        raise TypeError("value parameter is None")

    if param <= value:
        raise ValueError("{0} must be greater than {2} but got {1}".format(name, param, value))


def validate_less(name: str, param, value):
    if name is None:
        raise TypeError("name parameter is None")
    if param is None:
        raise TypeError("param parameter is None")
    if value is None:
        raise TypeError("value parameter is None")

    if param >= value:
            raise ValueError("{0} must be less than {2} but got {1}".format(name, param, value))

def validate_eq_greater(name: str, param, value):
    if name is None:
        raise TypeError("name parameter is None")
    if param is None:
        raise TypeError("param parameter is None")
    if value is None:
        raise TypeError("value parameter is None")

    if param < value:
            raise ValueError("{0} must be equal or greater than {2} but got {1}".format(name, param, value))

def validate_eq_less(name: str, param, value):
    if name is None:
        raise TypeError("name parameter is None")
    if param is None:
        raise TypeError("param parameter is None")
    if value is None:
        raise TypeError("value parameter is None")

    if param > value:
            raise ValueError("{0} must be equal or less than {2} but got {1}".format(name, param, value))

def validate_list(name: str, param, values: list):
    if name is None:
        raise TypeError("name parameter is None")
    if param is None:
        raise TypeError("param parameter is None")
    if values is None:
        raise TypeError("values parameter is None")

    if param not in values:
            raise ValueError("{0} must be in {2} but got {1}".format(name, param, values))

def validate_list(name: str, param, values: list):
    if name is None:
        raise TypeError("name parameter is None")
    if param is None:
        raise TypeError("param parameter is None")
    if values is None:
        raise TypeError("values parameter is None")

    if param not in values:
            raise ValueError("{0} must be in {2} but got {1}".format(name, param, values))


