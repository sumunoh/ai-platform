import h5py
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.model_selection import ShuffleSplit
import datetime as dt
import os



# 객체 생성
class write_main: 
  def __init__(self, input, target, index, folds):    # 데이터 연결
      self.input = input
      self.target = target
      self.index = index
      self.folds = folds
      

  def mkgd(self, filename, test_size, valid_test_rate):    # 그룹, 데이터셋 생성 
      mainfile = h5py.File(filename, 'w')
      data = mainfile.create_group("data")      
     
      input = data.create_dataset("input", data = self.input)
      target = data.create_dataset("target", data = self.target)
      index_group = np.arange(int(len(self.index)))
      train_test = ShuffleSplit(n_splits=self.folds, test_size=test_size, random_state=0)
      
      train=[]
      valid=[]
      test=[] 
      for train_index, test_index in train_test.split(index_group):
        train.append(train_index)
        slicing = round(len(test_index)*valid_test_rate)
        valid.append(test_index[:slicing])
        test.append(test_index[slicing:])
      
      index = mainfile.create_group("index")              
      for i in range(self.folds):
        globals() ['fold{}'.format(i+1)] = index.create_group('fold{}'.format(i+1))  
      
      print (list(index.keys()))
      
      for i,j in enumerate(index.keys()):
        globals() ['train'] = index[j].create_dataset('train', data = train[i])
        globals() ['valid'] = index[j].create_dataset('valid', data = valid[i])
        globals() ['test'] = index[j].create_dataset('test', data = test[i])




#a= write_main(inputs,targets,indexs, 5)
#a.mkgd('ir.h5', 0.3, 0.5)

