import h5py

class HDF5:                      
  def __init__(self, filename):
    mainfile = h5py.File(filename, 'r')
    self.mainfile = mainfile

  def load_data(self, dataset):
    data_get = self.mainfile.get('data')   
    input = data_get['input'][:]
    target = data_get['target'][:]

    if dataset == 'input':
      result=input
    elif dataset == 'target':
      result=target
    
    return result

  def load_index(self, fold_number, index):
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    result = index_get[index][:]  
    return result

  def train_input(self, fold_number, index):
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['train'][:]  
    va = list(va)
    
    data_get = self.mainfile.get('data')
    input = data_get['input'][index]

    return input

  def valid_input(self, fold_number, index):
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['valid'][:]  
    va = list(va)
    
    data_get = self.mainfile.get('data')
    input = data_get['input'][index]

    return input
    
  def test_input(self, fold_number, index):
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['test'][:]  
    va = list(va)
    
    data_get = self.mainfile.get('data')
    input = data_get['input'][index]

    return input

  def train_target(self, fold_number, index):
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['train'][:]  
    va = list(va)
    
    data_get = self.mainfile.get('data')
    target = data_get['target'][index]

    return target

  def valid_target(self, fold_number, index):
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['valid'][:]  
    va = list(va)
    
    data_get = self.mainfile.get('data')
    target = data_get['target'][index]

    return target

  def test_target(self, fold_number, index):
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['test'][:]  
    va = list(va)
    
    data_get = self.mainfile.get('data')
    target = data_get['target'][index]

    return target
