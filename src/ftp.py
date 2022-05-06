import ftplib
import os
import re
from src import exception

class FTP:
    def __init__(self, model_id: int, ip: str, port: int, id: str, pwd: str):
        exception.validate_type('model_id', model_id, int)
        exception.validate_eq_greater('model_id', model_id, 0)

        exception.validate_type('ip', ip, str)
        # add ip regular expresstion validate

        exception.validate_type('port', port, int)
        exception.validate_eq_greater('port', port, 0)

        exception.validate_type('id'. id, str)

        exception.validate_type('pwd', pwd, str)
        
        self.model_id = model_id
        self.ip = ip
        self.port = port
        self.id = id
        self.pwd = pwd
        self.ftp = ftplib.FTP()
        self.ftp.connect(host=self.ip, port=self.port)
        self.ftp.login(user=self.id, passwd=self.pwd)
        
    def mkdir_fold(self, fold:int):
        exception.validate_type('fold', fold, int)
        exception.validate_eq_greater('fold', fold, 1)

        parent_dir = '/{}'.format(self.model_id)
        self.ftp.mkd('{}'.format(parent_dir))

        for i in range(fold):
            fold_dir = '{}/fold{}'.format(parent_dir,i+1) 
            self.ftp.mkd(fold_dir)
            tensorboard_dir = '{}/tensorboard'.format(fold_dir)
            self.ftp.mkd(tensorboard_dir)
            epoch_dir = '{}/epoch'.format(fold_dir)
            self.ftp.mkd(epoch_dir)
        
    def save_metadata(self, source: str):
        exception.validate_type('source', source, str)

        self.ftp.cwd('/{}'.format(self.model_id))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR metadata{}'.format(extension), upload_file)
        upload_file.close()

    def save_tensorboard_train(self, source: str, fold: int):
        exception.validate_type('source', source, str)
        
        exception.validate_type('fold'. fold, int)
        exception.validate_eq_greater('fold', fold, 1)
        fold_list = self.ftp.nlst('/{}'.format(self.model_id))
        regex = re.compile('(\d+)(?!.*\d)')
        max_fold = int(regex.findall(fold_list[-1])[0])
        exception.validate_eq_less('fold', fold, max_fold)

        self.ftp.cwd('/{}/fold{}/tensorboard'.format(self.model_id, fold))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR train{}'.format(extension), upload_file)
        upload_file.close()
   
    def save_tensorboard_valid(self, source: str, fold: int):
        exception.validate_type('source', source, str)
        
        exception.validate_type('fold'. fold, int)
        exception.validate_eq_greater('fold', fold, 1)
        fold_list = self.ftp.nlst('/{}'.format(self.model_id))
        regex = re.compile('(\d+)(?!.*\d)')
        max_fold = int(regex.findall(fold_list[-1])[0])
        exception.validate_eq_less('fold', fold, max_fold)

        self.ftp.cwd('/{}/fold{}/tensorboard'.format(self.model_id, fold))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR valid{}'.format(extension), upload_file)
        upload_file.close()

    def save_epoch(self, source: str, fold: int, epoch: int):
        exception.validate_type('source', source, str)
        
        exception.validate_type('fold'. fold, int)
        exception.validate_eq_greater('fold', fold, 1)
        fold_list = self.ftp.nlst('/{}'.format(self.model_id))
        regex = re.compile('(\d+)(?!.*\d)')
        max_fold = int(regex.findall(fold_list[-1])[0])
        exception.validate_eq_less('fold', fold, max_fold)

        exception.validate_type('epoch', epoch, int)
        exception.validate_eq_greater('epoch', epoch, 0)

        self.ftp.cwd('/{}/fold{}/epoch'.format(self.model_id, fold))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR epoch{}{}'.format(epoch,extension), upload_file)
        upload_file.close()
