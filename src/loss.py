from abc import ABCMeta, abstractmethod
from torch.nn.functional import l1_loss
from torch import nn

class Loss(metaclass=ABCMeta):
    def __init__(self):
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
        super(L1Loss, self).__init__()

    def update(self, out, target):
        cnt = out.shape[0]
        loss = l1_loss(out, target)
        self.loss += loss * cnt
        self.count += cnt
        return loss

class BCELoss(Loss):
    def __init__(self):
        super(BCELoss, self).__init__()
        self.module = nn.BCELoss()

    def update(self, out, target):
        cnt = out.shape[0]
        loss = self.module(out, target)
        self.loss += loss.item() * cnt
        self.count += cnt
        return loss
