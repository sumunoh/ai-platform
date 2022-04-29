from src.data import schedule as _schedule
from src.data.constant import optimizer as _optimizer
from src.data.constant import loss as _loss
from src.data.constant import confusion_matrix as _confusion_matrix
from src.data.earlystop import MinMaxStop
from src.data import paramvalidation
from src.data.constant.metrics import METRICS

class Training:
    def __init__(self,  optimizer : str = _optimizer.ADAM, 
                        loss:str =_loss.MEAN_SQUARED_ERROR,
                        batch_size:int = 8, learning_rate:float=0.1, 
                        max_epoch:int=1000, early_stop:MinMaxStop = None,
                        learning_rate_schedule:_schedule.LearningSchedule = None,
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

        for param_name, param_type in param_hint:
               param_value=getattr(self, param_name)
               paramvalidation.validate_type(param_name, param_type, param_value)

        # range validate
        paramvalidation.validate_range_oneway('learning_rate', learning_rate, 0.0,'up') # 0.0 < learning_rate
        paramvalidation.validate_range_oneway('learning_rate', learning_rate, 1.0,'down') # 1.0 > learning_rate
        paramvalidation.validate_range_oneway('max_epoch', max_epoch,1,'eq_n_up') # 1 <= max epoch
        paramvalidation.validate_range_oneway('batch_size', batch_size,1,'eq_n_up')# 1 <= batch_size
        
        # mode validate
        paramvalidation.validate_mode('optimizer', optimizer, ['SGD', 'Adam', 'AdaDelta', 'AdaGrad', 'Adamax', 'Nadam', 'RMSprop'])
        paramvalidation.validate_mode('metrics',metrics, METRICS)
        
        
    def __iter__(self):
        
        yield 'optimizer', self.optimizer
        yield 'loss', self.loss
        yield 'batch size', self.batch_size
        yield 'learning_rate', self.learning_rate
        yield 'max_epoch', self.max_epoch
        yield 'early stop', dict(self.early_stop)
        yield 'learning rate schedule', dict(self.learning_rate_schedule)
        yield 'metrics',self.metrics


        
