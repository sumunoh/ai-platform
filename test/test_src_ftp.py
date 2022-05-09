import unittest
from src import ftp
#-*- coding: utf-8 -*- 
import ftplib
import os


class FTP(unittest.TestCase):
    def setUp(self):
        self.file_name = 'test_file.txt'
        with open(self.file_name, 'wt') as f:
            f.write("""
            단위테스트 검증용 파일
            """.strip())

        self.ftp = ftp.FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234')

    def tearDown(self):
        self._recursive_delete(self.ftp.ftp, '1234')

        try:
            os.remove(self.file_name)
        except:
            pass

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

    def _exist(self, ftp_client, name: str, root = ''):
        if os.path.join(root, name) in ftp_client.nlst(root):
            return True
        return False

    def test_mkdir_fold(self):
        f = ftp.FTP(2345, '10.1.1.65', 3021, 'ai', 'meta1234')
        f.mkdir_fold(5)

        ftp_clinet = ftplib.FTP()
        ftp_clinet.connect(host='10.1.1.65', port=3021)
        ftp_clinet.login(user='ai', passwd='meta1234')

        self.assertTrue(self._exist(ftp_clinet, '2345'))
         
        for i in range(5):
            self.assertTrue(self._exist(ftp_clinet, 'fold{}'.format(i + 1), '2345'))

            root = os.path.join('2345', 'fold{}'.format(i + 1))
            self.assertTrue(self._exist(ftp_clinet, 'tensorboard', root))
            self.assertTrue(self._exist(ftp_clinet, 'epoch', root))

    def test_mkdir_fold_double(self):
        f = ftp.FTP(3456, '10.1.1.65', 3021, 'ai', 'meta1234')
        f.mkdir_fold(5)
        f.mkdir_fold(5)

        self.assertTrue(True)

    def test_mkdir_fold_fold(self):
        ftp_client = self.ftp

        # type error
        error = None
        try:
            ftp_client.mkdir_fold(0.1)
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # value error
        error = None
        try:
            ftp_client.mkdir_fold(0)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

    def test_save_metadata(self):              
        f = self.ftp
        f.save_metadata('test_file.txt')       
        
        ftp = ftplib.FTP()
        ftp.connect(host='10.1.1.65', port=3021)
        ftp.login(user='ai', passwd='meta1234')
        
        self.assertTrue(self._exist(ftp, 'metadata.txt', '1234'))

    def test_save_metadata_source_error(self):
        # type error
        error = None
        try:
            self.ftp.save_metadata(1)
        except TypeError as e:
            error = e
        
        self.assertIsInstance(error, TypeError)

    def test_save_tensorboard_train(self):
        f = self.ftp
        f.save_tensorboard_train('test_file.txt', 1)
        
        ftp = ftplib.FTP()
        ftp.connect(host='10.1.1.65', port=3021)
        ftp.login(user='ai', passwd='meta1234')    

        self.assertTrue(self._exist(ftp, 'train.txt', '1234/fold1/tensorboard'))

    def test_save_tensorboard_train_source_error(self):
        # type error
        error = None
        try:
            self.ftp.save_tensorboard_train(-1, 1)
        except TypeError as e:
            error = e

        self.assertIsInstance(error, TypeError)

    def test_save_tensorboard_train_fold_error(self):
        # type error
        error = None
        try:
            self.ftp.save_tensorboard_train('test_file.txt', 'a')
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # undder error
        error = None
        try:
            self.ftp.save_tensorboard_train('test_file.txt', 0)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

        # over error
        error = None
        try:
            self.ftp.save_tensorboard_train('test_file.txt', 10)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

    def test_save_tensorboard_valid(self):
        f = self.ftp
        f.save_tensorboard_valid('test_file.txt', 1)       
        
        ftp = ftplib.FTP()
        ftp.connect(host='10.1.1.65', port=3021)
        ftp.login(user='ai', passwd='meta1234')

        self.assertTrue(self._exist(ftp, 'valid.txt', '1234/fold1/tensorboard'))

    def test_save_tensorboard_valid_fold_error(self):
        # type error
        error = None
        try:
            self.ftp.save_tensorboard_valid('test_file.txt', 'a')
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # undder error
        error = None
        try:
            self.ftp.save_tensorboard_valid('test_file.txt', 0)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

        # over error
        error = None
        try:
            self.ftp.save_tensorboard_valid('test_file.txt', 10)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

    def test_save_epoch(self):
        f = self.ftp
        f.save_epoch('test_file.txt', 1, 1)       
        
        ftp = ftplib.FTP()
        ftp.connect(host='10.1.1.65', port=3021)
        ftp.login(user='ai', passwd='meta1234')    

        self.assertTrue(self._exist(ftp, 'epoch_1.txt', '1234/fold1/epoch'))

    def test_save_epoch_source_error(self):
        # type error
        error = None
        try:
            self.ftp.save_epoch(1, 1, 1)
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

    def test_save_epoch_fold_error(self):
        # type error
        error = None
        try:
            self.ftp.save_epoch('test_file.txt', 'adsdf', 0)
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # undder error
        error = None
        try:
            self.ftp.save_epoch('test_file.txt', 0, 0)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

        # over error
        error = None
        try:
            self.ftp.save_epoch('test_file.txt', 10, 0)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

    def test_save_epoch_epoch_error(self):
        # type error
        error = None
        try:
            self.ftp.save_epoch('test_file.txt', 1, 'a')
        except TypeError as e:
            error = e
        self.assertIsInstance(error, TypeError)

        # under error
        error = None
        try:
            self.ftp.save_epoch('test_file.txt', 1, -1)
        except ValueError as e:
            error = e
        self.assertIsInstance(error, ValueError)

    def _recursive_delete(self, client, path):
        file_list = client.nlst(path)

        for file in file_list:
            name = os.path.basename(file)

            if '.' in name:
                client.delete(file)
            else:
                self._recursive_delete(client, file)
        client.rmd(path)

    

    @classmethod
    def tearDownClass(cls) -> None:
        clinet = ftplib.FTP()
        clinet.connect(host='10.1.1.65', port=3021)
        clinet.login(user='ai', passwd='meta1234')

        # cls._recursive_delete(cls.clinet, '1234')
        # cls._recursive_delete(cls.clinet, '2345')
        # cls._recursive_delete(cls.clinet, '3456')



# file_name = 'test_file.txt'
# with open(file_name, 'wt') as f:
#     f.write("""
#     단위테스트 검증용 파일
#     """.strip())

# ftp = ftp.FTP(1234, '10.1.1.65', 3021, 'ai', 'meta1234')
# ftp.save_tensorboard_train('test_file.txt', 10)