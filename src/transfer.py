from src.data import metadata, dataset as meta_dataset, training as meta_training
from src import dataset as torch_dataset
from torch.utils import data

def dataset_to_dataloader(dataset: meta_dataset.Dataset, training: meta_training.Training, dataset_type: str):
    return data.DataLoader(
        torch_dataset.Dataset(dataset.path_dataset, dataset.fold_number, dataset_type),
        batch_size=training.batch_size,
        shuffle=False,
        num_workers=dataset.num_worker,
        pin_memory=True,
        drop_last=True)
