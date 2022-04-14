from hdf5_mk import write_main
from hdf5_dao import HDF5
import h5py
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import KFold
import datetime as dt
import os


# 데이터 로드
iris = load_iris() 
iris_data = pd.DataFrame(iris.data, columns=iris.feature_names)
inputs=iris_data.copy()
iris_data.reset_index(inplace=True)
iris_data['class'] = iris.target
targets = iris_data['class']
indexs = iris_data['index']




#h5 파일 생성 
# h5_file= write_main(inputs,targets,indexs, 10)
# h5_file.mkgd('iris.h5', 0.3, 0.5)




# # dao 실행
# dao_run = HDF5('iris.h5')
# dao_run.load_index(3, 'train')
# dao_run.train_input(3,56)

