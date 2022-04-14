import h5py
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
from sklearn.model_selection import ShuffleSplit
import datetime as dt
import os




# dao
class HDF5:                      
  def __init__(self, filename):
    mainfile = h5py.File(filename, 'r')           # h5파일 읽기
    self.mainfile = mainfile


  def load_data(self, dataset):           # (input or target) 전체 데이터 조회
    data_get = self.mainfile.get('data')   
    input = data_get['input'][:]
    target = data_get['target'][:]

    if dataset == 'input':
      result=input
    elif dataset == 'target':
      result=target
    
    return result


  def load_index(self, fold_number, index):        # 특정 fold그룹의 (train or valid or test) index값만 조회
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    result = index_get[index][:]  
    return result




  def train_input(self, fold_number, index):      # 특정 fold그룹의 index별 train input 데이터
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['train'][:]  
    va = list(va)
    
    if index in va:
      data_get = self.mainfile.get('data')
      input = data_get['input'][index]
    else:
      input = print('인덱스값이 존재하지 않습니다.')

    return input



  def valid_input(self, fold_number, index):     # 특정 fold그룹의 index별 valid input 데이터
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['valid'][:]  
    va = list(va)
    
    if index in va:
      data_get = self.mainfile.get('data')
      input = data_get['input'][index]
    else:
      input = print('인덱스값이 존재하지 않습니다.')

    return input


    
  def test_input(self, fold_number, index):     # 특정 fold그룹의 index별 test input 데이터
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['test'][:]  
    va = list(va)
    
    if index in va:
      data_get = self.mainfile.get('data')
      input = data_get['input'][index]
    else:
      input = print('인덱스값이 존재하지 않습니다.')

    return input



  def train_target(self, fold_number, index):     # 특정 fold그룹의 index별 train  target 데이터
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['train'][:]  
    va = list(va)
    
    if index in va:
      data_get = self.mainfile.get('data')
      target = data_get['target'][index]
    else:
      target = print('인덱스값이 존재하지 않습니다.')

    return target



  def valid_target(self, fold_number, index):     # 특정 fold그룹의 index별 valid target 데이터
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['valid'][:]  
    va = list(va)
    
    if index in va:
      data_get = self.mainfile.get('data')
      target = data_get['target'][index]
    else:
      target = print('인덱스값이 존재하지 않습니다.')

    return target

    

  def test_target(self, fold_number, index):     # 특정 fold그룹의 index별 test target 데이터
    index_get = self.mainfile.get('index/fold{}'.format(fold_number))     
    va = index_get['test'][:]  
    va = list(va)
    
    if index in va:
      data_get = self.mainfile.get('data')
      target = data_get['target'][index]
    else:
      target = print('인덱스값이 존재하지 않습니다.')

    return target





# _h5 = HDF5('iris.h5')
# _h5.load_index(3, 'test')
# _h5.test_target(3, 23)
