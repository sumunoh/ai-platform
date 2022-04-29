import h5py

class HDF5:                      
  def __init__(self, filename):
    mainfile = h5py.File(filename, 'r')
    self.mainfile = mainfile

  def load_data(self, data):
    data_get = self.mainfile.get('data')   
    input = data_get['input'][:]
    target = data_get['target'][:]

    if data == 'input':
      result=input
    elif data == 'target':
      result=target
    return result

  def load_index(self, fold_number, dataset):
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    result = index_get[dataset][:]  
    
    return result

  def load_input(self, fold_number, index):  
    data_get = self.mainfile.get('data')
    input = data_get['input'][index]

    return input

  def load_target(self, fold_number, index):
    data_get = self.mainfile.get('data')
    target = data_get['target'][index]

    return target