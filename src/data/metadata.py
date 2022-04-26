import src.data.dataset as _dataset
import src.data.model as _model
import src.data.training as _training

class Metadata:
    def __init__(self, dataset, model, training) -> None:
        self.dataset : _dataset.Dataset =dataset
        self.model : _model.Model = model
        self.training : _training.Training = training
        
    def __iter__(self):
        
        yield 'dataset', dict(self.dataset)
        yield 'model', dict(self.model)
        yield 'training', dict(self.training)
