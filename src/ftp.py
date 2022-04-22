#-*- coding: utf-8 -*- 

import os

class model_result:
    def __init__(self,ID):   
        iddir =  (os.path.abspath('/home/vsftpd/ai/model_n')) +'/{}'.format(ID)
        print('폴더 경로:', iddir)
        if os.path.exists(iddir):
            print('모델 식별자 {} 폴더가 이미 존재합니다.'.format(ID))
        else:       
            os.mkdir(iddir)
            print('모델 식별자 {} 폴더를 생성합니다.'.format(ID))
            self.iddir =iddir
            print()

    def mkdir_fold(self, fold):
        for i in range(fold):
            folddir = os.path.dirname(os.path.abspath('{}/fold_n').format(self.iddir)) +'/fold{}/tensorboard'.format(i+1)
            os.mkdir(folddir)




a = model_result(123)
a.mkdir_fold(5)
