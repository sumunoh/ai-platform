from src.data import schedule as _schedule
from src.data.constant import optimizer as _optimizer
from src.data.constant import loss as _loss
from src.data.constant import confusion_matrix as _confusion_matrix
import src.data.earlystop as _earlystop
from src.data import paramvalidation
from src.data.constant.metrics import METRICS

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


        #type validate
        param_hint = list(self.__init__.__annotations__.items())[:-1]
        except_params=['early_stop', 'learning_rate_schedule']

        for param_name, param_type in param_hint:
            if not param_name in except_params:
               param_value=getattr(self, param_name)
               paramvalidation.validate_type(param_name, param_type, param_value)

        # range validate
        paramvalidation.validate_range('learning_rate', learning_rate,0,1)
        paramvalidation.validate_range('max_epoch', max_epoch,0,1000)
        
        # mode validate
        
        paramvalidation.validate_mode('optimizer', optimizer, ['SGD', 'Adam', 'AdaDelta', 'AdaGrad', 'Adamax', 'Nadam', 'RMSprop'])

    def __iter__(self):
        
        yield 'optimizer', self.optimizer
        yield 'loss', self.loss
        yield 'batch size', self.batch_size
        yield 'learning_rate', self.learning_rate
        yield 'max_epoch', self.max_epoch
        yield 'early stop', dict(self.early_stop)
        yield 'learning rate schedule', dict(self.learning_rate_schedule)
        yield 'metrics',self.metrics


        
