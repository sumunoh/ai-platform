from pickletools import optimize
import unittest
from src import process, loss
from src.data.constant import initializer as const_initializer, optimizer as const_optimizer, loss as const_loss, metrics as const_metrics
import torch
from torch.utils import data
import tempfile
import os
from src.data import metadata, dataset, training, model
import h5py
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
    def test_trainprocess(self):
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
            torch.nn.Sigmoid()
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

class Test_MetaTrainProcess(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.filename = os.path.join(self.dir.name, 'hdf5.h5')

        h5 = h5py.File(self.filename, 'w')

        data_group = h5.create_group('data')
        data_group.create_dataset('input', data=[[0., 0.], [0., 1.], [1., 0.], [1., 1.]], dtype=float)
        data_group.create_dataset('target', data=[[0], [1], [1], [0]], dtype=float)

        index_group = h5.create_group('index')

        fold1_group = index_group.create_group('fold1')
        fold1_group.create_dataset('train', data=[0, 1, 2, 3])
        fold1_group.create_dataset('valid', data=[0, 1, 2, 3])
        fold1_group.create_dataset('test', data=[0, 1, 2, 3])

        fold2_group = index_group.create_group('fold2')
        fold2_group.create_dataset('train', data=[0, 1, 2, 3])
        fold2_group.create_dataset('valid', data=[0, 1, 2, 3])
        fold2_group.create_dataset('test', data=[0, 1, 2, 3])

        h5.close()

        return super().setUp()

    def test_process(self):
        proc = process.MetaTrainProcess()

        meta = metadata.Metadata(
            dataset.Dataset('', self.filename, 2, 1),
            model.Model(
                model.InputLayer(2),
                model.OutputLayer(1),
                '',
                '',
                const_initializer.RANDOM_NORMAL
            ),
            training.Training(
                optimizer=const_optimizer.SGD,
                loss=const_loss.BINARY_CROSS_ENTROPY_ERROR,
                batch_size=1,
                learning_rate=0.1,
                max_epoch=10,
                early_stop=None,
                learning_rate_schedule=None,
                metrics=const_metrics.confusion_matrix.ACCURACY
            )
        )

        proc.run(meta)

        return self.assertTrue(True)
