from turtle import down
from src.data import paramvalidation
from src.data.constant.metrics import METRICS

class MinMaxStop:
    def __init__(self, mode:str, monitor:str, min_delta:float, patience:int):
        
        # type validation
        paramvalidation.validate_type('mode', str, mode)
        paramvalidation.validate_type('monitor', str, monitor)
        paramvalidation.validate_type('min_delta', float, min_delta)
        paramvalidation.validate_type('patience', int, patience)
        
        
        # range validation
        paramvalidation.validate_eq_n_greater('patience', patience, 1)
        paramvalidation.validate_greater('min_delta', min_delta, 0.0)
        
        
        # mode validation
        valid_mode={'min','max'}
        paramvalidation.validate_mode('mode', mode, valid_mode)
        paramvalidation.validate_mode('monitor', monitor, METRICS)

        self.mode =mode
        self.monitor = monitor
        self.min_delta = min_delta
        self.patience = patience
        
    def __iter__(self):
        
        yield 'mode', self.mode
        yield 'monitor', self.monitor
        yield 'min delta', self.min_delta
        yield 'patience', self.patience