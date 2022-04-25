from abc import ABCMeta
from src.data.constant import schedule as _schedule
from src.data import paramvalidation

class LearningSchedule(metaclass=ABCMeta):
    def __init__(self, schedule_type: str) -> None:
        super().__init__()
        self._tpye = schedule_type

    @property
    def schedule_tpye(self):
        return self._tpye

    
    def __iter__(self):
        yield 'schedule type', self._tpye

class ConstantSchedule(LearningSchedule):
    def __init__(self) -> None:
        super().__init__(_schedule.CONSTANT)

class MulytiplySchedule(LearningSchedule):
    def __init__(self, multi: float = 0.1) -> None:
        super().__init__(_schedule.MULTIPLY)
        self._multi = multi
        paramvalidation.validate_range('multi', multi,0,1)

    @property
    def multi(self):
        return self._multi

    def __iter__(self):
        for p in super(MulytiplySchedule, self).__iter__():
            yield p 
        yield 'multi', self._multi

class ExpotentialSchedule(LearningSchedule):
    def __init__(self, x:float) -> None:
        super().__init__(_schedule.EXPOTENTIAL)
        self._Expotential = x
        
    def __iter__(self):
        for p in super(ExpotentialSchedule, self).__iter__():
            yield p
        yield 'x', self._Expotential
        
