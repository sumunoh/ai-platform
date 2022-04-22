import loss
from dataset import Dataset
from torch.utils.data import DataLoader
import torch

class TrainProcess:
    def __init__(self) -> None:
        pass

    def _setup(self):
        # 학습 하기 전 환경 설정
        # 쿠다, 데이터 저장 폴더, 로그 폴더 등...
        pass

    def _build_dataset(self):
        # hdf5 파일을 읽는 데이터 로드 생성, train, valid, test에 대해서 하나씩
        dataset = Dataset('path', 0, 'train')
        dataloader = DataLoader(
            dataset,
            batch_size=8,
            shuffle=True,
            num_workers=1,
            pin_memory=True,
            drop_last=True)
        pass

    def _build_model(self, device: torch.device):
        # 메타데이터에 따라 model, optimizer, scheduler 생성
        model = None

        optimizer = torch.optim.SGD(model.parameters(), 0.001)

        scheduler = torch.optim.lr_scheduler.MultiStepLR(optimizer, 10, 0.99)

        return model, optimizer, scheduler

    def _train_model(train_loader, model, loss: loss.Loss, optimizer, scheduler, device):
        # 학습 진행
        model.train()

        for epoch in range(100):
            loss.reset()
            for input, target in train_loader:
                input = input.to(device)
                target = target.to(device)

                output = model(input)

                loss_value = loss.update(output, target)

                loss_value.backward()
                optimizer.step()


            scheduler.step()

        # checkpoint



    def run(self):
        self._setup()
        self._build_dataset()
        model, optimizer, scheduler = self._build_model(None)
        self._train_model(model, None, optimizer, scheduler, None)
