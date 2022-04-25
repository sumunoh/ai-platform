from src.data import paramvalidation

class InputLayer:
    def __init__(self, size:int):
        
        paramvalidation.validate_type('InputLayer',int, size)

        self.size = size
                
    def __iter__(self):
        yield 'size', self.size
    
class OutputLayer:
    def __init__(self, size:int, activation:str = 'sigmoid'):

        if not isinstance(size, int) :
                paramvalidation.validate_type('size', int, size)

        paramvalidation.validate_type('activation', str, activation)

        valid_activation = {'sigmoid', 'ReLU', 'softmax'}

        paramvalidation.validate_mode('activation', activation, valid_activation)

        self.size = size
        self.activation = activation


    def __iter__(self):
        yield 'size', self.size
        yield 'activate', self.activation