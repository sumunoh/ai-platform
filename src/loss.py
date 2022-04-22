from abc import ABCMeta, abstractmethod
from torch.nn.functional import l1_loss

class Loss(metadata=ABCMeta):
    def __init__(self):
        super().__init__()
        self.loss = 0
        self.count = 0

    @abstractmethod
    def update(self, out, target):
        pass

    def reset(self):
        self.loss = 0
        self.count = 0

    def result(self):
        return self.loss / self.count

class L1Loss(Loss):
    def __init__(self):
        super().__init__()

    def update(self, out, target):
        cnt = out.shape[0]
        loss = l1_loss(out, target)
        self.loss += loss * cnt
        self.count += cnt
        return loss
