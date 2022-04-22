import unittest
from src import process, loss
import torch
from torch.utils import data
import tempfile
import os
from torch.utils.tensorboard import SummaryWriter

class XORDataset(data.Dataset):
    def __init__(self) -> None:
        self.x = torch.FloatTensor([[0, 0], [0, 1], [1, 0], [1, 1]])
        self.y = torch.FloatTensor([[0], [1], [1], [0]])

    def __len__(self):
        return 4

    def __getitem__(self, index):
        return self.x[index], self.y[index]

class Test_TrainProcess(unittest.TestCase):
    def test_run(self):
        proc = process.TrainProcess()

        train_dir = tempfile.TemporaryDirectory()
        valid_dir = tempfile.TemporaryDirectory()
        checkpoint = tempfile.TemporaryDirectory()
        model = torch.nn.Sequential(
            torch.nn.Linear(2, 10),
            torch.nn.Sigmoid(),
            torch.nn.Linear(10, 10),
            torch.nn.Sigmoid(),
            torch.nn.Linear(10, 10),
            torch.nn.Sigmoid(),
            torch.nn.Linear(10, 1),
            torch.nn. 
            Sigmoid()
        )
        optimizer = torch.optim.SGD(model.parameters(), lr=1)
        proc.run(
            data.DataLoader(XORDataset()),
            data.DataLoader(XORDataset()),
            SummaryWriter(train_dir.name),
            SummaryWriter(valid_dir.name),
            model,
            optimizer,
            loss.BCELoss(),
            10,
            checkpoint.name
        )

        return self.assertTrue(True)