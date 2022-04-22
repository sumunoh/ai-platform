from importlib import import_module
from torch.utils import data

class Dataset(data.Dataset):
    def __init__(self, file: str, num: int, set_type: str) -> None:
        super().__init__()

    def __getitem__(self, index):
        # torch 객체로 input과 target을 반환
        return super().__getitem__(index)

    def __len__(self):
        # 총 길이 반환
        return 0
