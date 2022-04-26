from src.data import paramvalidation

class InputLayer:
    def __init__(self, size:int): 
        #type validation
        paramvalidation.validate_type('InputLayer',int, size)
        
        # range validation
        paramvalidation.validate_range_oneway('size',size, 1, 'down')
        
        self.size = size
                    
    def __iter__(self):
        yield 'size', self.size
    
class OutputLayer:
    def __init__(self, size:int, activation:str = 'sigmoid'):

        #type validation
        if not isinstance(size, int) :
                paramvalidation.validate_type('size', int, size)
        paramvalidation.validate_type('activation', str, activation)
                
        # range validation
        paramvalidation.validate_range_oneway('size',size, 1, 'down')
                
        # mode validation
        valid_activation = {'sigmoid', 'ReLU', 'softmax'}
        paramvalidation.validate_mode('activation', activation, valid_activation)

        self.size = size
        self.activation = activation


    def __iter__(self):
        yield 'size', self.size
        yield 'activate', self.activation