#-*- coding: utf-8 -*- 

import os
import shutil

class model_result:
# 모델 식별자 폴더 생성(중복성 검증)  
   def __init__(self, id):
      id_dir = '/home/vsftpd/ai'+'/{}'.format(id) 
      if os.path.exists(id_dir):
          print('모델 식별자 {} 폴더가 이미 존재합니다.'.format(id))
      else:       
          os.mkdir(id_dir)
          print('모델 식별자 {} 폴더를 생성합니다.'.format(id))
          self.id_dir = id_dir


# 초기 폴더 생성 기능 
   def mkdir_fold(self, fold_n):
      for i in range(fold_n):
        fold_dir = '{}/fold{}'.format(self.id_dir,i+1) 
        os.mkdir(fold_dir)
        tensorboard_dir = '{}/tensorboard'.format(fold_dir)
        os.mkdir(tensorboard_dir)
        epoch_dir = '{}/epoch'.format(fold_dir)
        os.mkdir(epoch_dir)


# metadata 파일 위치를 받아 지정된 위치에 저장
   def cd_metadata(self, source, name):
      root, extension = os.path.splitext(source)
      destination = r'{}/{}{}'.format(self.id_dir, name, extension)
      shutil.move(source,destination)


# 학습용 데이터 텐서보드 파일 저장
   def cd_train(self, source, fold):
      root, extension = os.path.splitext(source)
      destination = r'{}/fold{}/tensorboard/train{}'.format(self.id_dir,extension)
      shutil.move(source,destination)


# 검증용 데이터 텐서보드 파일 저장
   def cd_valid(self, source, fold):
      root, extension = os.path.splitext(source)
      destination = r'{}/fold{}/tensorboard/valid{}'.format(self.id_dir,extension)
      shutil.move(source,destination)


# 저장된 모델 파일 위치를 받아 지정된 위치에 저장
   def cd_epoch(self, source, fold, epoch):
      root, extension = os.path.splitext(source)
      destination = r'{}/fold{}/epoch/epoch{}{}'.format(self.id_dir, epoch, extension)
      shutil.move(source,destination)




# a = model_result(12345)
# a.mkdir_fold(5)
# a.cd_metadata('/home/vsftpd/abc.h5')
