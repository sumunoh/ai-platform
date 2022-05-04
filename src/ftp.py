#-*- coding: utf-8 -*- 
import ftplib
import os
import re
# import sys 
# sys.path.insert(0, '../src')
from src import dao_exception

class FTP:
    def __init__(self, uniq_id: int, ip: str, port: int, id: str, pwd: str):

        int_ = [uniq_id, port]
        str_ = [ip, id, pwd]
        
        for i in int_:
            dao_exception.dao_type("{}".format(i), i, int)
 
        for i in str_:
            dao_exception.dao_type("{}".format(i), i, str)

        for i in int_:
            dao_exception.dao_range_oneway("{}".format(i), i, 0, 'eq_n_up')
        
        self.uniq_id = uniq_id
        self.ip = ip
        self.port = port
        self.id = id
        self.pwd = pwd
        self.ftp = ftplib.FTP()
        self.ftp.connect(host=self.ip, port=self.port)
        self.ftp.login(user=self.id, passwd=self.pwd)
        


    def mkdir_fold(self, fold:int):
        parent_dir = '/{}'.format(self.uniq_id)
        self.ftp.mkd('{}'.format(parent_dir))
        
        dao_exception.dao_type("fold", fold, int)
        dao_exception.dao_range_oneway("fold", fold, 0, 'eq_n_up')

        for i in range(fold):
            fold_dir = '{}/fold{}'.format(parent_dir,i+1) 
            self.ftp.mkd(fold_dir)
            tensorboard_dir = '{}/tensorboard'.format(fold_dir)
            self.ftp.mkd(tensorboard_dir)
            epoch_dir = '{}/epoch'.format(fold_dir)
            self.ftp.mkd(epoch_dir)

        
    # metadata 파일 위치를 받아 지정된 위치에 저장
    def save_metadata(self, source: str):              
        
        dao_exception.dao_type("source", source, str)

        self.ftp.cwd('/{}'.format(self.uniq_id))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR metadata{}'.format(extension), upload_file)


    # 학습용 데이터 텐서보드 파일 저장
    def save_TensorboardTrain(self, source: str, fold_n: int):
        dao_exception.dao_type("source", source, str)
        dao_exception.dao_type("fold_n", fold_n, int)

        fold_list = self.ftp.nlst('/{}'.format(self.uniq_id))
        regex = re.compile('(\d+)(?!.*\d)')
        max_fold = int(regex.findall(fold_list[-1])[0])

        dao_exception.dao_range("fold_n", fold_n, 1, max_fold)

        self.ftp.cwd('/{}/fold{}/tensorboard'.format(self.uniq_id, fold_n))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR train{}'.format(extension), upload_file)

    

    # 검증용 데이터 텐서보드 파일 저장
    def save_TensorboardValid(self, source: str, fold_n: int):
        dao_exception.dao_type("source", source, str)
        dao_exception.dao_type("fold_n", fold_n, int)

        fold_list = self.ftp.nlst('/{}'.format(self.uniq_id))
        regex = re.compile('(\d+)(?!.*\d)')
        max_fold = int(regex.findall(fold_list[-1])[0])

        dao_exception.dao_range("fold_n", fold_n, 1, max_fold)

        self.ftp.cwd('/{}/fold{}/tensorboard'.format(self.uniq_id, fold_n))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR valid{}'.format(extension), upload_file)


    # 저장된 모델 파일 위치를 받아 지정된 위치에 저장
    def save_epoch(self, source: str, fold_n: int, epoch_n: int):
        dao_exception.dao_type("source", source, str)
        dao_exception.dao_type("fold_n", fold_n, int)
        dao_exception.dao_type("epoch_n", epoch_n, int)

        fold_list = self.ftp.nlst('/{}'.format(self.uniq_id))
        regex = re.compile('(\d+)(?!.*\d)')
        max_fold = int(regex.findall(fold_list[-1])[0])

        dao_exception.dao_range("fold_n", fold_n, 1, max_fold)
        dao_exception.dao_range_oneway("fold_n", fold_n, 1, max_fold)
        self.ftp.cwd('/{}/fold{}/epoch'.format(self.uniq_id, fold_n))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR epoch{}{}'.format(epoch_n,extension), upload_file)




#f = FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234')
#f.mkdir_fold(5)
# f.save_metadata('test_file.txt')
#f.save_TensorboardTrain('/dev/work/ai-platform-1/src/iris.h5', 3)
# f.save_TensorboardValid('test_file.txt', 3)
# f.save_epoch('test_file.txt', 3, 3)
