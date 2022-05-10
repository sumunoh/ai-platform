import ftplib
import os
import re
from src import exception

class FTP:
    def __init__(self, model_id: int, max_fold: int, ip: str, port: int, id: str, pwd: str):
        exception.validate_type('model_id', model_id, int)
        exception.validate_eq_greater('model_id', model_id, 0)

        exception.validate_type('max_fold', max_fold, int)
        exception.validate_eq_greater('max_fold', max_fold, 1)

        exception.validate_type('ip', ip, str, 'ip')
        # add ip regular expresstion validate

        exception.validate_type('port', port, int)
        exception.validate_eq_greater('port', port, 0)

        exception.validate_type('id', id, str)

        exception.validate_type('pwd', pwd, str)
        
        self.model_id = model_id
        self.max_fold = max_fold
        self.ip = ip
        self.port = port
        self.id = id
        self.pwd = pwd
        self.ftp = ftplib.FTP()
        self.ftp.connect(host=self.ip, port=self.port)
        self.ftp.login(user=self.id, passwd=self.pwd)

    def _exist(self, name: str, root = ''):
        if os.path.join(root, name) in self.ftp.nlst(root):
            return True
        return False


    def save_metadata(self, source: str):
        exception.validate_type('source', source, str)

        if not self._exist('{}'.format(self.model_id)):
            self.ftp.mkd('{}'.format(self.model_id))

        self.ftp.cwd('/{}'.format(self.model_id))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR metadata{}'.format(extension), upload_file)
        upload_file.close()

    def save_tensorboard_train(self, source: str, fold: int):
        exception.validate_type('source', source, str)        
        exception.validate_type('fold', fold, int)
        exception.validate_eq_greater('fold', fold, 1)
        exception.validate_eq_less('fold', fold, self.max_fold)
              
        self.ftp.cwd('/{}'.format(self.model_id))
        if not self._exist('fold{}'.format(fold)):
            self.ftp.mkd('fold{}'.format(fold))
            
        self.ftp.cwd('/{}/fold{}'.format(self.model_id, fold))        
        if not self._exist('tensorboard'):
            self.ftp.mkd('tensorboard')           

        self.ftp.cwd('/{}/fold{}/tensorboard'.format(self.model_id, fold))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR train{}'.format(extension), upload_file)
        upload_file.close()
   
   
    def save_tensorboard_valid(self, source: str, fold: int):
        exception.validate_type('source', source, str)        
        exception.validate_type('fold', fold, int)
        exception.validate_eq_greater('fold', fold, 1)
        exception.validate_eq_less('fold', fold, self.max_fold)
              
        self.ftp.cwd('/{}'.format(self.model_id))
        if not self._exist('fold{}'.format(fold)):
            self.ftp.mkd('fold{}'.format(fold))
            
        self.ftp.cwd('/{}/fold{}'.format(self.model_id, fold))        
        if not self._exist('tensorboard'):
            self.ftp.mkd('tensorboard')           

        self.ftp.cwd('/{}/fold{}/tensorboard'.format(self.model_id, fold))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR valid{}'.format(extension), upload_file)
        upload_file.close()


    def save_epoch(self, source: str, fold: int, epoch: int):
        exception.validate_type('source', source, str)      
        exception.validate_type('fold', fold, int)
        exception.validate_eq_greater('fold', fold, 1)
        exception.validate_eq_less('fold', fold, self.max_fold)
        exception.validate_type('epoch', epoch, int)
        exception.validate_eq_greater('epoch', epoch, 0)

        self.ftp.cwd('/{}'.format(self.model_id))
        if not self._exist('fold{}'.format(fold)):
            self.ftp.mkd('fold{}'.format(fold))
            
        self.ftp.cwd('/{}/fold{}'.format(self.model_id, fold))        
        if not self._exist('epoch'):
            self.ftp.mkd('epoch')           

        self.ftp.cwd('/{}/fold{}/epoch'.format(self.model_id, fold))
        root, extension = os.path.splitext(source)    
        upload_file = open(source, 'rb')    
        self.ftp.storbinary('STOR epoch{}{}'.format(epoch, extension), upload_file)
        upload_file.close()
