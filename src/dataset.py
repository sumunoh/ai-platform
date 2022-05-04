from torch.utils import data
from src import hdf5
import torch

class Dataset(data.Dataset):
    def __init__(self, file: str, num: int, set_type: str) -> None:
        super().__init__()
        self.hdf5 = hdf5.HDF5(file)
        self.num = num
        self.set_type = set_type
        self.index = self.hdf5.mainfile['index/fold{}/{}'.format(self.num, self.set_type)]

    def __getitem__(self, index):
        input = None
        target = None

        if self.set_type == 'train':
            input = self.hdf5.train_input(self.num, self.index[index])
            target = self.hdf5.train_input(self.num, self.index[index])
        elif self.set_type == 'valid':
            input = self.hdf5.valid_input(self.num, self.index[index])
            target = self.hdf5.valid_input(self.num, self.index[index])
        elif self.set_type == 'test':
            input = self.hdf5.test_input(self.num, self.index[index])
            target = self.hdf5.test_input(self.num, self.index[index])

        return torch.from_numpy(input), torch.from_numpy(target)

    def __len__(self):
        return len(self.index)
