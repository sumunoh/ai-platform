from src.data import metadata, dataset as meta_dataset, training as meta_training
from src.data.constant import optimizer as const_optimizer, loss as const_loss
from src import dataset as torch_dataset, loss as torch_loss
from torch.utils import data
import tempfile
import torch

def dataset_to_dataloader(dataset: meta_dataset.Dataset, training: meta_training.Training, dataset_type: str):
    train_loader = data.DataLoader(
        torch_dataset.Dataset(dataset.path_dataset, dataset.fold_number, 'train'),
        batch_size=training.batch_size,
        shuffle=True,
        num_workers=dataset.num_worker,
        pin_memory=True,
        drop_last=True)

    valid_loader = data.DataLoader(
        torch_dataset.Dataset(dataset.path_dataset, dataset.fold_number, 'valid'),
        batch_size=training.batch_size,
        shuffle=False,
        num_workers=dataset.num_worker,
        pin_memory=True,
        drop_last=False)

    return train_loader, valid_loader

def meta_to_optimizer(params, training: meta_training.Training):
    if training.optimizer == const_optimizer.SGD:
        return torch.optim.SGD(params, training.learning_rate)
    elif training.optimizer == const_optimizer.ADAM:
        return torch.optim.Adam(params, training.learning_rate)

def meta_to_loss(training: meta_training.Training):
    if training.loss == const_loss.BINARY_CROSS_ENTROPY_ERROR:
        return torch_loss.BCELoss()
