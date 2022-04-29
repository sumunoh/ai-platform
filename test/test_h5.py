import unittest
from hdf5 import HDF5
import h5py
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import ShuffleSplit
import datetime as dt
import numpy as np
import os


class test_h5(unittest.TestCase):



    def setUp(self):
        """테스트 시작되기 전 파일 작성"""

        iris = load_iris() 
        iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
        inputs=iris_data.copy()
        iris_data.reset_index(inplace=True)
        iris_data['class'] = iris.target
        targets = iris_data['class']
        indexs = iris_data['index']

        test_file = h5py.File('test_file.h5', 'w')
        data = test_file.create_group("data")      
        
        input = data.create_dataset("input", data = inputs)
        target = data.create_dataset("target", data = targets)
        index_group = np.arange(int(len(indexs)))
        train_test = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
        
        train=[]
        valid=[]
        test=[] 
        for train_index, test_index in train_test.split(index_group):
            train.append(train_index)
            slicing = round(len(test_index)*0.5)
            valid.append(test_index[:slicing])
            test.append(test_index[slicing:])
        
        folds = 5

        index = test_file.create_group("index")              
        for i in range(folds):
            globals() ['fold{}'.format(i+1)] = index.create_group('fold{}'.format(i+1))  
        
        
        for i,j in enumerate(index.keys()):
            globals() ['train'] = index[j].create_dataset('train', data = train[i])
            globals() ['valid'] = index[j].create_dataset('valid', data = valid[i])
            globals() ['test'] = index[j].create_dataset('test', data = test[i])

        test_file.close()
   

    def test_load_data_input(self):
        h5 = HDF5('test_file.h5')
        a = h5.load_data('input')

        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r')
        data = hdf.get('data') 
        b = data['input'][:] 

        self.assertEqual(a.any(),b.any())


    def test_load_data_target(self):
        h5 = HDF5('test_file.h5')
        a = h5.load_data('target')

        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        data = hdf.get('data') 
        b = data['target'][:] 

        self.assertEqual(a.any(),b.any())



    def test_load_index_train(self):
        h5 = HDF5('test_file.h5')
        a = h5.load_index(1, 'train')

        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        index_ = hdf.get('index/fold1') 
        b = index_['train'][:] 

        self.assertEqual(a.any(),b.any())



    def test_load_index_valid(self):
        h5 = HDF5('test_file.h5')
        a = h5.load_index(1, 'valid')

        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        index_ = hdf.get('index/fold1') 
        b = index_['valid'][:] 

        self.assertEqual(a.any(),b.any())



    def test_load_index_test(self):
        h5 = HDF5('test_file.h5')
        a = h5.load_index(1, 'test')

        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        index_ = hdf.get('index/fold1') 
        b = index_['test'][:] 

        self.assertEqual(a.any(),b.any())


    def test_load_input(self):
        h5 = HDF5('test_file.h5')
        a = h5.load_input(1, 1)
        
        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        data_get = hdf.get('data')
        b = data_get['input'][1]

        self.assertEqual(a.any(),b.any())


    def test_load_target(self):
        h5 = HDF5('test_file.h5')
        a = h5.load_target(1, 1)
        
        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        data_get = hdf.get('data')
        b = data_get['target'][1]

        self.assertEqual(a.any(),b.any())


    def tearDown(self):
        """테스트 종료 후 파일 삭제 """
        try:
            os.remove("test_file.h5")
        except:
            pass

if __name__ == '__main__':
    unittest.main()