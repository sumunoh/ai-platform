from abc import ABCMeta, abstractmethod
from data.constant import metrics

class Metrics(metadata=ABCMeta):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def update(self, out, target):
        pass

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def result(self):
        pass


class Accuracy(Metrics):
    def __init__(self) -> None:
        super().__init__(metrics.ACCURACY)
        self.num = 0
        self.collect = 0

    def update(self, out, target):
        label_pred = 0
        label_true = 0
        self.collect += 0
        self.num += len(out)

    def reset(self):
        self.collect = 0
        self.num = 0

    def result(self):
        return self.collect / self.num
