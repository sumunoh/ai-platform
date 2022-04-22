import paramvalidation
from layer import InputLayer, OutputLayer
class Model():
    # path
    # layer 추가필요
    def __init__(self,input_layer:InputLayer, output_layer:OutputLayer, path_model_save:str, name:str, initializer:str='random normal',gpu:bool=True):

        self.input_layer=input_layer
        self.output_layer=output_layer
        # self.path=path
        # self.layer=layer
        self.path_model_save= path_model_save
        self.name = name
        self.initializer =initializer
        self.gpu = gpu

        param_info = list(self.__init__.__annotations__.items())[:-1]
        except_params = ['input_layer', 'output_layer']
        for param_name, param_type in param_info:
            if not param_name in except_params:
                param_value=getattr(self, param_name)
                paramvalidation.validate_type(param_name, param_type, param_value)

    def __iter__(self):
        yield 'input layer', dict(self.input_layer)
        yield 'output layer', dict(self.output_layer) 
        # yield 'path', self.path
        # yield 'layer', self.layer
        yield 'path model save', self.path_model_save
        yield 'name', self.name
        yield 'initializer',self.initializer
        yield 'gpu', self.gpu        
        
        

        
        
# class NetPath(Model):
#     def __init__(self):
#         pass
    
# class NetWork(Model):
#     def __init__(self):
#         pass