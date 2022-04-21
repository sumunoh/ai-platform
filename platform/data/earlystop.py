import paramvalidation
from constant.metrics import METRICS
class MinMaxStop:
    def __init__(self, mode:str, monitor:str, min_delta:float, patience:int):
        
        valid_mode={'min','max'}
        paramvalidation.validate_type('mode', str, mode)
        paramvalidation.validate_mode('mode',mode, valid_mode)
        self.mode =mode

        paramvalidation.validate_type('monitor', str, monitor)
        paramvalidation.validate_mode('mode',monitor, METRICS)
        self.monitor = monitor

        paramvalidation.validate_type('min_delta', float, min_delta)
        self.min_delta = min_delta

        paramvalidation.validate_type('patience', int, patience)
        self.patience = patience
        
    def __iter__(self):
        
        yield 'mode', self.mode
        yield 'monitor', self.monitor
        yield 'min delta', self.min_delta
        yield 'patience', self.patience