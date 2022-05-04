import unittest
# import sys 
# sys.path.insert(0, '../src')

from src.ftp import FTP
#-*- coding: utf-8 -*- 
import ftplib
import os




class test_ftp(unittest.TestCase):


    def setUp(self):
        """테스트 시작되기 전 파일 작성"""
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'wt') as f:
            f.write("""
            단위테스트 검증용 파일
            """.strip())
            
        f.close()



    def test_mkdir_fold(self):
        f = FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234')    
        f.mkdir_fold(5)

        ftp = ftplib.FTP()
        ftp.connect(host='10.1.1.65', port=3021)
        ftp.login(user='ai', passwd='meta1234')
         
        for i in range(5):
            ftp.rmd("1234/fold{}/tensorboard".format(i+1))
            ftp.rmd("1234/fold{}/epoch".format(i+1))
            ftp.rmd("1234/fold{}".format(i+1))
            
        ftp.rmd('1234')
    

    def test_save_metadata(self):              
        f = FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234') 
        f.mkdir_fold(5)
        f.save_metadata('test_file.txt')       
        
        ftp = ftplib.FTP()
        ftp.connect(host='10.1.1.65', port=3021)
        ftp.login(user='ai', passwd='meta1234')
        
        
        for i in range(5):
            ftp.rmd("1234/fold{}/tensorboard".format(i+1))
            ftp.rmd("1234/fold{}/epoch".format(i+1))
            ftp.rmd("1234/fold{}".format(i+1))

        ftp.cwd('1234')
        ftp.delete("metadata.txt")
        ftp.cwd('/')  
        ftp.rmd('1234')

        

    def test_save_TensorboardTrain(self):
        f = FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234') 
        f.mkdir_fold(5)
        f.save_TensorboardTrain('test_file.txt',1)       
        
        ftp = ftplib.FTP()
        ftp.connect(host='10.1.1.65', port=3021)
        ftp.login(user='ai', passwd='meta1234')    

        ftp.cwd('1234/fold1/tensorboard')
        ftp.delete("train.txt")
        ftp.cwd('/')
        for i in range(5):
            ftp.rmd("1234/fold{}/tensorboard".format(i+1))
            ftp.rmd("1234/fold{}/epoch".format(i+1))
            ftp.rmd("1234/fold{}".format(i+1))

        ftp.cwd('/')  
        ftp.rmd('1234')


    

    def test_save_TensorboardValid(self):
        f = FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234') 
        f.mkdir_fold(5)
        f.save_TensorboardValid('test_file.txt',1)       
        
        ftp = ftplib.FTP()
        ftp.connect(host='10.1.1.65', port=3021)
        ftp.login(user='ai', passwd='meta1234')    

        ftp.cwd('1234/fold1/tensorboard')
        ftp.delete("valid.txt")
        ftp.cwd('/')
        for i in range(5):
            ftp.rmd("1234/fold{}/tensorboard".format(i+1))
            ftp.rmd("1234/fold{}/epoch".format(i+1))
            ftp.rmd("1234/fold{}".format(i+1))

        ftp.cwd('/')  
        ftp.rmd('1234')


    def test_save_epoch(self):
        f = FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234') 
        f.mkdir_fold(5)
        f.save_epoch('test_file.txt',1,1)       
        
        ftp = ftplib.FTP()
        ftp.connect(host='10.1.1.65', port=3021)
        ftp.login(user='ai', passwd='meta1234')    

        ftp.cwd('1234/fold1/epoch')
        ftp.delete("epoch1.txt")
        ftp.cwd('/')
        for i in range(5):
            ftp.rmd("1234/fold{}/tensorboard".format(i+1))
            ftp.rmd("1234/fold{}/epoch".format(i+1))
            ftp.rmd("1234/fold{}".format(i+1))

        ftp.cwd('/')  
        ftp.rmd('1234')


    def tearDown(self):
        """테스트 종료 후 파일 삭제 """
        try:
            os.remove(self.file_name)
            
        except:
            pass


if __name__ == '__main__':
    unittest.main()