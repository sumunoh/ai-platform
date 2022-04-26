import src.data.dataset as _dataset
import src.data.model as _model
import src.data.training as _training
from src.data import paramvalidation
class Metadata:
    def __init__(self, dataset:_dataset.Dataset, model:_model.Model, training:_training.Training):
        
        #type validation
        paramvalidation.validate_type('dataset', _dataset.Dataset, dataset)
        paramvalidation.validate_type('model', _model.Model, model)
        paramvalidation.validate_type('training', _training.Training, training)
        
        
        self.model : _model.Model = model
        self.dataset : _dataset.Dataset =dataset
        self.training : _training.Training = training
        
    def __iter__(self):
        
        yield 'dataset', dict(self.dataset)
        yield 'model', dict(self.model)
        yield 'training', dict(self.training)


#부분부터 시작.
# data.model.py
# input_layer, output_layer에 대한 class type 검사 추가
# initializer 범위 검사