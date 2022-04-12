class MinMaxStop:
    def __init__(self, mode:str, monitor:str, min_delta:float, patience:int):
        self.mode =mode
        self.monitor = monitor
        self.min_delta = min_delta
        self.patience = patience
        
    def __iter__(self):
        
        yield 'mode', self.mode
        yield 'monitor', self.monitor
        yield 'min delta', self.min_delta
        yield 'patience', self.patience