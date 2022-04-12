class Model:
    # path
    # layer 추가필요
    def __init__(self,input_layer, output_layer, path_model_save, name, initializer='random normal',gpu=True):
        
        self.input_layer=input_layer
        self.output_layer=output_layer
        # self.path=path
        # self.layer=layer
        self.path_model_save= path_model_save
        self.name = name
        self.initializer =initializer
        self.gpu = gpu
    
    def __iter__(self):
        yield 'input layer', dict(self.input_layer)
        yield 'output layer', dict(self.output_layer) 
        # yield 'path', self.path
        # yield 'layer', self.layer
        yield 'path model save', self.path_model_save
        yield 'name', self.name
        yield 'initializer',self.initializer
        yield 'gpu', self.gpu        
        
        
class InputLayer:
    def __init__(self, size):
        self.size = size
        
    def __iter__(self):
        yield 'size', self.size
    
    
class OutputLayer:
    def __init__(self, size, activation = 'sigmoid'):
        self.size = size
        self.activate = activation
        
    def __iter__(self):
        yield 'size', self.size
        yield 'activate', self.activate
        
        
# class NetPath(Model):
#     def __init__(self):
#         pass
    
# class NetWork(Model):
#     def __init__(self):
#         pass