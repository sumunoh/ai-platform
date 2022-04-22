from tabnanny import check
from src import loss
from src import dataset
from torch.utils import data
import torch
import os
from torch.utils.tensorboard import SummaryWriter

class TrainProcess:
    def __init__(self) -> None:
        pass

    def _setup(self):
        # 학습 하기 전 환경 설정
        # 쿠다, 데이터 저장 폴더, 로그 폴더 등...
        self.train_loader: data.DataLoader = None
        self.valid_loader: data.DataLoader = None
        self.train_summary: SummaryWriter = None
        self.valid_summary: SummaryWriter = None
        self.model: torch.nn.Module = None
        self.optimizer: torch.optim.Optimizer = None
        self.loss: loss.Loss = None
        self.checkpoint: str = None

    def _forward_model(self, input, target):
        output = self.model(input)
        loss = self.loss.update(output, target)
        return loss

    def _train_model(self):
        self.model.train()

        for input, target in self.train_loader:
            loss = self._forward_model(input, target)

            loss.backward()
            self.optimizer.step()
        
        return self.loss.result()

    def _valid_model(self):
        self.model.eval()

        for input, target in self.valid_loader:
            loss = self._forward_model(input, target)

        return self.loss.result()

    def _summary(self, train_loss, valid_loss, step):
        self.train_summary.add_scalar('loss', train_loss, step)
        self.valid_summary.add_scalar('loss', valid_loss, step)

    def _save(self, epoch):
        path = os.path.join(self.checkpoint, '{}.tar'.format(epoch))
        torch.save(
            {'model': self.model.state_dict()},
            path
        )

    def run(
        self,
        train_loader: data.DataLoader,
        valid_loader: data.DataLoader,
        train_summary: SummaryWriter,
        valid_summary: SummaryWriter,
        model: torch.nn.Module,
        optimizer: torch.optim.Optimizer,
        loss: loss.Loss,
        max_epoch: int,
        checkpoint: str):

        self.train_loader = train_loader
        self.valid_loader = valid_loader
        self.train_summary = train_summary
        self.valid_summary = valid_summary
        self.model = model
        self.optimizer = optimizer
        self.loss = loss
        self.checkpoint = checkpoint

        for epoch in range(max_epoch):
            self.loss.reset()

            train_loss = self._train_model()
            valid_loss = self._valid_model()
            self._summary(train_loss, valid_loss, epoch)
            self._save(epoch)
