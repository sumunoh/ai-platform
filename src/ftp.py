#-*- coding: utf-8 -*- 
import ftplib
import os

class FTP:
    def __init__(self, uniq_id: None, ip: str, port: int, id: str, pwd: str):
        self.uniq_id = uniq_id
        self.ip = ip
        self.port = port
        self.id = id
        self.pwd = pwd
        self.ftp = ftplib.FTP()
        self.ftp.connect(host=self.ip, port=self.port)
        self.ftp.login(user=self.id, passwd=self.pwd)
        
        parent_dir = '/{}'.format(self.uniq_id)
        self.ftp.mkd('{}'.format(parent_dir))
        self.parent_dir = parent_dir


    def mkdir_fold(self, fold_n:int):
      for i in range(fold_n):
        fold_dir = '{}/fold{}'.format(self.parent_dir,i+1) 
        self.ftp.mkd(fold_dir)
        tensorboard_dir = '{}/tensorboard'.format(fold_dir)
        self.ftp.mkd(tensorboard_dir)
        epoch_dir = '{}/epoch'.format(fold_dir)
        self.ftp.mkd(epoch_dir)

    
    # metadata 파일 위치를 받아 지정된 위치에 저장
    def save_metadata(self, source: str):              
        self.ftp.cwd('/{}'.format(self.uniq_id))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR metadata{}'.format(extension), upload_file)


    # 학습용 데이터 텐서보드 파일 저장
    def save_TensorboardTrain(self, source: str, fold: int):
        self.ftp.cwd('/{}/fold{}/tensorboard'.format(self.uniq_id, fold))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR train{}'.format(extension), upload_file)

    

    # 검증용 데이터 텐서보드 파일 저장
    def save_TensorboardValid(self, source: str, fold: int):
        self.ftp.cwd('/{}/fold{}/tensorboard'.format(self.uniq_id, fold))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR valid{}'.format(extension), upload_file)


    # 저장된 모델 파일 위치를 받아 지정된 위치에 저장
    def save_epoch(self, source: str, fold: int, epoch: int):
        self.ftp.cwd('/{}/fold{}/epoch'.format(self.uniq_id, fold))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR epoch{}{}'.format(epoch,extension), upload_file)








# f = FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234')
# f.mkdir_fold(5)
# f.save_metadata('/dev/work/ai-platform-1/src/test1.csv')
# f.save_TensorboardTrain('/dev/work/ai-platform-1/src/test2.csv', 3)
# f.save_TensorboardValid('/dev/work/ai-platform-1/src/test1.csv', 3)
# f.save_epoch('/dev/work/ai-platform-1/src/test1.csv', 3, 3)
