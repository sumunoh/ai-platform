import unittest
from src.api.manage import app
import requests

class ApiTests(unittest.TestCase):
    
    
    def setUp(self) -> None:
        self.app = app.test_client()
        
        self.host = 'http://localhost:5555'
        
        
        #right_parameters 
        self.data_dataset = {"dataset type":'h5',"path dataset":"./data_dir",
                            "fold size":1, "fold number":1, "num worker":1,"random seed":1
                        }

        self.data_model ={'input layer':{'size':10}, 'output layer':{'size':10, 'activation':'softmax'},
                    'path model save':'./dir','name':'my_model','initializer':'random normal','gpu':False}

        self.data_training = {'optimizer':'Adam','loss':"mean squared error", 'batch size':1, 'learning rate':0.1, 'max epoch': 2, 
                    'early stop':{'mode':'min','monitor':'accuracy','min delta':0.1,'patience':1}, 'learning rate schedule':{'schedule type':'Constant'},
                    'metrics':'accuracy'}

        #wrong_parameters
    
    # def metadata 파라미터 정의()
    # def metadata 타입 검사()
    # def metadata 범위 검사()
    # def metadata 모드 검사()
    # def metadata 필수 검사()
    
    
    # def dataset 파라미터 정의()
    # def dataset 타입 검사()
    # def dataset 범위 검사()
    # def metadata 모드 검사()
    # def dataset 필수 검사()
    
    # def model 파라미터 정의()
    # def model 타입 검사()
    # def model 범위 검사()
    # def metadata 모드 검사()
    # def model 필수 검사()
    
    
    # def training 파라미터 정의()
    # def training 타입 검사
    # def training 범위 검사
    # def metadata 모드 검사
    # def training 필수 검사
    
    
    def test_right_dataset_param(self):
        """dataset_param 판별하는 테스트 메소드"""
        
        response = requests.post(self.host + '/meta/dataset', json = self.data_dataset)
        data = response.json()
        self.assertEqual(200, data['status code'])
        
def custom_function():
    pass

if __name__ == '__main__':
    unittest.main()