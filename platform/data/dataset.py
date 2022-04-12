class Dataset:
    def __init__(self, dataset_type:str, path_dataset:str=None,
                       fold_size=5, fold_num=None, num_worker=1,random_seed=7777777) -> None:
        
        self.dataset_type = dataset_type
        self.path_dataset=path_dataset
        self.fold_size = fold_size
        self.fold_num = fold_num
        self.num_worker = num_worker
        self.random_seed = random_seed
        
    def __iter__(self):
        yield 'dataset type', self.dataset_type
        yield 'path dataset', self.path_dataset
        yield 'fold size', self.fold_size
        yield 'fold num', self.fold_num
        yield 'num worker', self.num_worker
        yield 'random seed', self.random_seed
        
