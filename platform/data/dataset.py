import paramvalidation
class Dataset:
    def __init__(self, dataset_type:str, path_dataset:str=None,
                       fold_size:int=5, fold_number:int=None, num_worker:int=1,random_seed:int=7777777) -> None:

        params = [dataset_type, path_dataset, fold_size, fold_number, num_worker, random_seed]
        param_hint = list(self.__init__.__annotations__.items())[:-1]
        for idx, param in enumerate(param_hint):
            param_name, param_type = param
            param_value = params[idx]
            paramvalidation.validate_type(param_name, param_type, param_value)

        self.dataset_type = dataset_type
        self.path_dataset=path_dataset
        self.fold_size = fold_size
        self.fold_number = fold_number
        self.num_worker = num_worker
        self.random_seed = random_seed


    def __iter__(self):
        yield 'dataset type', self.dataset_type
        yield 'path dataset', self.path_dataset
        yield 'fold size', self.fold_size
        yield 'fold number', self.fold_number
        yield 'num worker', self.num_worker
        yield 'random seed', self.random_seed
        