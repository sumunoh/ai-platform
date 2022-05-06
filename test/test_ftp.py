from msilib.schema import Error
import unittest
from src import ftp
#-*- coding: utf-8 -*- 
import ftplib
import os


class FTP(unittest.TestCase):
    def setUp(self):
        """테스트 시작되기 전 파일 작성"""
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'wt') as f:
            f.write("""
            단위테스트 검증용 파일
            """.strip())
            
        f.close()

    def test_ftp(self):
        ftp.FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234')

        self.assertTrue(True)

    def test_ftp_model_id_error(self):
        # type error
        error = None
        try:
            ftp.FTP(0.1, '10.1.1.65', 3021, 'ai', 'meta1234')
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # value error
        error = None
        try:
            ftp.FTP(-1, '10.1.1.65', 3021, 'ai', 'meta1234')
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

    def test_ftp_ip_error(self):
        # type error
        error = None
        try:
            ftp.FTP(1234, 10, 3021, 'ai', 'meta1234')
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

    def test_ftp_port_error(self):
        # type error
        error = None
        try:
            ftp.FTP(1234, '10.1.1.65', 0.1, 'ai', 'meta1234')
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # value error
        error = None
        try:
            ftp.FTP(1234, '10.1.1.65', -1, 'ai', 'meta1234')
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

    def test_ftp_id_error(self):
        # type error
        error = None
        try:
            ftp.FTP(1234, '10.1.1.65', 3021, -1, 'meta1234')
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

    def test_ftp_pwd_error(self):
        # type error
        error = None
        try:
            ftp.FTP(1234, '10.1.1.65', 3021, 'ai', -1)
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

    def test_mkdir_fold(self):
        f = ftp.FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234')
        f.mkdir_fold(5)

        ftp = ftplib.FTP()
        ftp.connect(host='10.1.1.65', port=3021)
        ftp.login(user='ai', passwd='meta1234')
         
        for i in range(5):
            ftp.rmd("1234/fold{}/tensorboard".format(i+1))
            ftp.rmd("1234/fold{}/epoch".format(i+1))
            ftp.rmd("1234/fold{}".format(i+1))
            
        ftp.rmd('1234')

    def test_mkdir_fold_fold(self):
        ftp_dao = ftp.FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234')

        # type error
        error = None
        try:
            ftp_dao.mkdir_fold(0.1)
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # value error
        error = None
        try:
            ftp_dao.mkdir_fold(0)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

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