from abc import ABCMeta, abstractmethod

class LearningSchedule(metaclass=ABCMeta):
    def __init__(self, rate: float) -> None:
        self.original_rate = rate
        self.rate = rate

    @abstractmethod
    def update(self):
        pass


class ConstantSchedule(LearningSchedule):
    def __init__(self, rate: float) -> None:
        super().__init__(rate)


class MultiplySchedule(LearningSchedule):
    def __init__(self, rate: float, multi: float) -> None:
        super().__init__(rate)
        self.multi = multi

    def update(self):
        self.rate = self.rate * self.multi
