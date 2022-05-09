import unittest
from src import hdf5
import h5py
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import ShuffleSplit
import numpy as np
import os

class HDF5(unittest.TestCase):
    def setUp(self):
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

        self.h5 = hdf5.HDF5('test_file.h5')

    def test_init(self):
        h5 = hdf5.HDF5('test_file.h5')

        self.assertTrue(True)

    def test_init_filename_error(self):
        # type error
        error = None
        try:
            h5 = hdf5.HDF5(-1)
        except TypeError as e:
            error = e
        
        self.assertIsInstance(error, TypeError)

    def test_load_data_input(self):
        h5 = self.h5
        a = h5.load_data('input')

        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r')
        data = hdf.get('data') 
        b = data['input'][:] 

        self.assertEqual(a.any(),b.any())

    def test_load_data_target(self):
        h5 = self.h5
        a = h5.load_data('target')

        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        data = hdf.get('data') 
        b = data['target'][:] 

        self.assertEqual(a.any(),b.any())

    def test_load_data_data_error(self):
        h5 = self.h5

        # type error
        error = None
        try:
            h5.load_data(1)
        except TypeError as e:
            error = e

        self.assertIsInstance(error, TypeError)

        # value error
        error = None
        try:
            h5.load_data('asdf')
        except ValueError as e:
            error = e

        self.assertIsInstance(error, ValueError)

    def test_load_index_train(self):
        h5 = self.h5
        a = h5.load_index(1, 'train')

        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        index_ = hdf.get('index/fold1') 
        b = index_['train'][:] 

        self.assertEqual(a.any(),b.any())

    def test_load_index_valid(self):
        h5 = self.h5
        a = h5.load_index(1, 'valid')

        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        index_ = hdf.get('index/fold1') 
        b = index_['valid'][:] 

        self.assertEqual(a.any(),b.any())

    def test_load_index_test(self):
        h5 = self.h5
        a = h5.load_index(1, 'test')

        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        index_ = hdf.get('index/fold1') 
        b = index_['test'][:] 

        self.assertEqual(a.any(),b.any())

    def test_load_index_fold_error(self):
        h5 = self.h5

        # type error
        error = None
        try:
            h5.load_index(0.1, 'train')
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # under error
        error = None
        try:
            h5.load_index(0, 'train')
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

        # over error
        error = None
        try:
            h5.load_index(6, 'train')
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

    def test_load_index_dataset_error(self):
        h5 = self.h5

        # type error
        error = None
        try:
            h5.load_index(1, 1)
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # value error
        error = None
        try:
            h5.load_index(1, 'asdf')
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

    def test_load_input(self):
        h5 = self.h5
        a = h5.load_input(1)
        
        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        data_get = hdf.get('data')
        b = data_get['input'][1]

        self.assertEqual(a.any(),b.any())

    def test_load_input_index_error(self):
        h5 = self.h5

        # type error
        error = None
        try:
            h5.load_input(0.1)
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # value error
        error = None
        try:
            h5.load_input(-1)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)


    def test_load_target(self):
        h5 = self.h5
        a = h5.load_target(1)
        
        filename ='test_file.h5'
        hdf = h5py.File(filename, 'r') 
        data_get = hdf.get('data')
        b = data_get['target'][1]

        self.assertEqual(a.any(),b.any())

    def test_load_target_index_error(self):
        h5 = self.h5

        # type error
        error = None
        try:
            h5.load_target(0.1)
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # value error
        error = None
        try:
            h5.load_target(-1)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

    def tearDown(self):
        try:
            os.remove("test_file.h5")
        except:
            pass


