class Dataset:
    def __init__(self, fold_size=5, fold_num=None) -> None:
        self.fold_size = fold_size
        self.fold_num = fold_num

    def __iter__(self):
        yield 'fold size', self.fold_size
        yield 'fold num', self.fold_num
