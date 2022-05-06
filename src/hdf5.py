import h5py
from src import exception
import re

class HDF5:                      
  def __init__(self, filename: str):
    exception.validate_type('filename', filename, str)

    self.mainfile = h5py.File(filename, 'r')
    index_= self.mainfile.get('index')
    ls = list(index_.keys())
    max_fold = int(re.findall(r'\d+', ls[len(ls)-1])[0])
    self.max_fold = max_fold

  def load_data(self, data: str):
    exception.validate_type('data', data, str)
    exception.validate_list('data', data, ['input', 'target'])

    data_get = self.mainfile.get('data')   
    input = data_get['input'][:]
    target = data_get['target'][:]
    
    if data == 'input':
      result=input
    elif data == 'target':
      result=target
    
    return result

  def load_index(self, fold: int, dataset: str):
    exception.validate_type('fold', fold, int)
    exception.validate_eq_greater('fold', fold, 1)
    exception.validate_eq_less('fold', fold, self.max_fold)

    exception.validate_type('dataset', dataset, str)
    exception.validate_list('dataset', dataset, ['train', 'valid', 'test'])

    index_get = self.mainfile.get('index/fold{}'.format(fold))     
    result = index_get[dataset][:]  
    
    return result

  def load_input(self, index: int):  
    exception.validate_type('index', index, int)
    exception.validate_eq_greater('index', index, 0)
    
    data_get = self.mainfile.get('data')
    input = data_get['input'][index]

    return input

  def load_target(self, index: int):
    exception.validate_type('index', index, int)
    exception.validate_eq_greater('index', index, 0)

    data_get = self.mainfile.get('data')
    target = data_get['target'][index]

    return target
