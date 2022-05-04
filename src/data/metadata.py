from src.data import dataset as _dataset
from src.data import model as _model
from src.data import training as _training

class Metadata:
    def __init__(self, dataset, model, training) -> None:
        self.dataset : _dataset.Dataset =dataset
        self.model : _model.Model = model
        self.training : _training.Training = training
        
    def __iter__(self):
        
        yield 'dataset', dict(self.dataset)
        yield 'model', dict(self.model)
        yield 'training', dict(self.training)

