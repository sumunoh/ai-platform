import schedule as _schedule
from constant import optimizer as _optimizer
from constant import loss as _loss
from constant import confusion_matrix as _confusion_matrix
import earlystop as _earlystop


class Training:
    def __init__(self,  optimizer : str = _optimizer.ADAM, 
                        loss:str =_loss.MEAN_SQUARED_ERROR,
                        batch_size:int = 8, learning_rate:float=0.1, 
                        max_epoch:int=1000, early_stop:_earlystop = None,
                        learning_rate_schedule:_schedule = None,
                        metrics:str = _confusion_matrix.ACCURACY):
        
        self.optimizer = optimizer
        self.loss = loss
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.max_epoch = max_epoch
        self.early_stop = early_stop
        self.learning_rate_schedule=learning_rate_schedule
        self.metrics = metrics
        
    def __iter__(self):
        
        yield 'optimizer', self.optimizer
        yield 'loss', self.loss
        yield 'batch size', self.batch_size
        yield 'learning_rate', self.learning_rate
        yield 'max_epoch', self.max_epoch
        yield 'early stop', dict(self.early_stop)
        yield 'learning rate schedule', dict(self.learning_rate_schedule)
        yield 'metrics',self.metrics


        
