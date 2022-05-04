import h5py
# import sys 
# sys.path.insert(0, '../src')
from src import dao_exception
import re

class HDF5:                      
  def __init__(self, filename):
    dao_exception.dao_type('filename', filename, str)
    mainfile = h5py.File(filename, 'r')
    self.mainfile = mainfile
    index_= self.mainfile.get('index')
    ls = list(index_.keys())
    max_fold = int(re.findall(r'\d+', ls[len(ls)-1])[0])
    self.max_fold = max_fold


  def load_data(self, data:str):
    dao_exception.dao_mode('data', data,['input', 'target'])
    data_get = self.mainfile.get('data')   
    input = data_get['input'][:]
    target = data_get['target'][:]
    
    if data == 'input':
      result=input
    elif data == 'target':
      result=target
    
    return result


  def load_index(self, fold_n:int, dataset:str):
    dao_exception.dao_type('fold_n', fold_n, int)
    dao_exception.dao_range('fold_n', fold_n, 1, self.max_fold)
    dao_exception.dao_type('dataset', dataset, str)

    index_get = self.mainfile.get('index/fold{}'.format(fold_n))     
    result = index_get[dataset][:]  
    
    return result


  def load_input(self, index:int):  
    dao_exception.dao_type('index', index, int)
    
    data_get = self.mainfile.get('data')
    max_index = len(data_get['input'][:])
    dao_exception.dao_range_oneway('index', index, max_index, 'down')
    
    input = data_get['input'][index]


    return input

  def load_target(self, index:int):
    dao_exception.dao_type('index', index, int)

    data_get = self.mainfile.get('data')
    max_index = len(data_get['target'][:])
    
    dao_exception.dao_range_oneway('index', index, max_index, 'down')
    target = data_get['target'][index]

    return target



# h = HDF5('iris.h5')
# h.load_target(0)
