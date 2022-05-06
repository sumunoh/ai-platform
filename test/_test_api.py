import sys
# sys.path.append("/dev/AIpf/work/ai-platform")
import unittest

from src.api.manage import app
import requests

class UnitTest(unittest.TestCase):
    
    def setUp(self) -> None:
        
        self.app = app.test_client()
        
        self.host = 'http://localhost:5555'
        
        #right_parameters 
        self.param_dataset = {"dataset type":'h5',"path dataset":"./data_dir",
                              "fold size":1, "fold number":1, "num worker":1,"random seed":1}

        self.param_model ={'input layer':{'size':10}, 'output layer':{'size':10, 'activation':'softmax'},
                           'path model save':'./dir','name':'my_model','initializer':'random normal','gpu':False}

        self.param_training = {'optimizer':'Adam','loss':"mean squared error", 'batch size':1, 'learning rate':0.1, 'max epoch': 2, 
                               'early stop':{'mode':'min','monitor':'accuracy','min delta':0.1,'patience':1}, 'learning rate schedule':{'schedule type':'Constant'},
                               'metrics':'accuracy'}

        #wrong_parameters
        
    # 연결 설정 -> return responses
    
    def connect_with_param(self, url, params):
        response = requests.post(self.host + url, json = params)
        data = response.json()
        return data
    
    # test _ url _ T/F _ parameter name _ test name
    def test_dataset_right_parameters(self):
        url = '/meta/dataset'
        params = self.param_dataset
        data =  self.connect_with_param(url,params)
        self.assertEqual(200, data['status code'], data)
        
    #str-> test:int
    def test_dataset_wrong_dataset_type_type(self):
        url = '/meta/dataset'
        params = self.param_dataset
        params['dataset type']=1
        data = self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
    
    #str->test:int
    def test_dataset_wrong_path_dataset_type(self):
        url = '/meta/dataset'
        params = self.param_dataset
        params['path dataset']=1
        data = self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])

    #int->test:float
    def test_dataset_wrong_fold_size_type(self):
        url = '/meta/dataset'
        params = self.param_dataset
        params['fold size']=1.0
        data = self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
    #int->test:float
    def test_dataset_wrong_fold_number_type(self):
        url = '/meta/dataset'
        params = self.param_dataset
        params['fold number']=1.0
        data = self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
    #int->test:float
    def test_dataset_wrong_num_worker_type(self):
        url = '/meta/dataset'
        params = self.param_dataset
        params['num worker']=1.0
        data = self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
    #int->test:float
    def test_dataset_wrong_random_seed_type(self):
        url = '/meta/dataset'
        params = self.param_dataset
        params['random seed']=1.0
        data = self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
    
    # def dataset 범위 검사()
    def test_dataset_wrong_fold_size_range(self):
        url = '/meta/dataset'
        params = self.param_dataset
        params['fold size']=-1
        data = self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])    
                
    def test_dataset_wrong_num_worker_range(self):
        url = '/meta/dataset'
        params = self.param_dataset
        params['num worker']=-1
        data = self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])    
        
    def test_dataset_wrong_random_seed_range(self):
        url = '/meta/dataset'
        params = self.param_dataset
        params['random seed']=-2**63-1
        data = self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])    
                                    
    
    # def dataset 필수 검사()
    # def model 파라미터 정의()
    def test_model_right_parameters(self):
        url = '/meta/model'
        params = self.param_model
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    # def model 타입 검사()
    

    #input layer (class) -> test:str
    def test_model_wrong_input_layer_type(self):
        url = '/meta/model'
        params = self.param_model
        params['input layer']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
        
    #input layer[size] (int) ->test:str
    def test_model_wrong_input_layer_size_type(self):
        url = '/meta/model'
        params = self.param_model
        params['input layer']['size']='100'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
    #output layer(class) -> test:str
    def test_model_wrong_output_layer_type(self):
        url = '/meta/model'
        params = self.param_model
        params['output layer']='100'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
        
    #output layer[size](int) -> test:str
    def test_model_wrong_output_layer_size_type(self):
        url = '/meta/model'
        params = self.param_model
        params['output layer']['size']='100'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
    #output layer[activation](str) -> test:int
    def test_model_wrong_output_layer_activation_type(self):
        url = '/meta/model'
        params = self.param_model
        params['output layer']['activation']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
    #path model save(str) -> test:int
    def test_model_wrong_path_model_save_type(self):
        url = '/meta/model'
        params = self.param_model
        params['path model save']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
    #name(str) -> test:int
    def test_model_wrong_name_type(self):
        url = '/meta/model'
        params = self.param_model
        params['name']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
    #initializer(str) -> test:int
    def test_model_wrong_initializer_type(self):
        url = '/meta/model'
        params = self.param_model
        params['initializer']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
    
    #gpu(bool) -> test:str
    def test_model_wrong_gpu_type(self):
        url = '/meta/model'
        params = self.param_model
        params['gpu']='1'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
    
    # def model range test
    def test_model_wrong_input_layer_size_range(self):
        url = '/meta/model'
        params = self.param_model
        params['input layer']['size'] = 0
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])

    def test_model_wrong_output_layer_size_range(self):
        url = '/meta/model'
        params = self.param_model
        params['output layer']['size'] = 0
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
    # def model 모드 검사()
    def test_model_wrong_output_layer_activation_mode(self):
        url = '/meta/model'
        params = self.param_model
        params['output layer']['activation'] = 'function x'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])
        
        
    def test_model_wrong_initializer_mode(self):
        url = '/meta/model'
        params = self.param_model
        params['initialize'] = 'linear123'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data['error message'])

    # def training 타입 검사
    def test_training_right_parameters(self):
        url = '/meta/training'
        params = self.param_training
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
    
    def test_training_wrong_optimizer_type(self):
        url = '/meta/training'
        params = self.param_training
        params['optimizer']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_loss_type(self):
        url = '/meta/training'
        params = self.param_training
        params['loss']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_batch_size_type(self):
        url = '/meta/training'
        params = self.param_training
        params['batch size']='100'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_learning_rate_type(self):
        url = '/meta/training'
        params = self.param_training
        params['learning rate']='100'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_max_epoch_type(self):
        url = '/meta/training'
        params = self.param_training
        params['max epoch']='100'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_early_stop_type(self):
        url = '/meta/training'
        params = self.param_training
        params['early stop']='100'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_early_stop_mode_type(self):
        url = '/meta/training'
        params = self.param_training
        params['early stop']['mode']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_early_stop_monitor_type(self):
        url = '/meta/training'
        params = self.param_training
        params['early stop']['monitor']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_early_stop_min_delta_type(self):
        url = '/meta/training'
        params = self.param_training
        params['early stop']['min delta']='100'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_early_stop_patience_type(self):
        url = '/meta/training'
        params = self.param_training
        params['early stop']['patience']='100'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_learning_rate_schedule_type(self):
        url = '/meta/training'
        params = self.param_training
        params['learning rate schedule']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_learning_rate_schedule_schedule_type_type(self):
        url = '/meta/training'
        params = self.param_training
        params['learning rate schedule']['schedule type']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_metrics_type(self):
        url = '/meta/training'
        params = self.param_training
        params['metrics']=100
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)


    
    # def training 범위 검사
    def test_training_wrong_batch_size_range(self):
        url = '/meta/training'
        params = self.param_training
        params['batch size']=0
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_learning_rate_range(self):
        url = '/meta/training'
        params = self.param_training
        params['learning rate']=0
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_max_epoch_range(self):
        url = '/meta/training'
        params = self.param_training
        params['max epoch']=0
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_early_stop_min_delta_range(self):
        url = '/meta/training'
        params = self.param_training
        params['early stop']['min delta']=0
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)

    def test_training_wrong_early_stop_patience_range(self):
        url = '/meta/training'
        params = self.param_training
        params['early stop']['patience']=0
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
    
    # def metadata 모드 검사
    def test_training_wrong_optimizer_mode(self):
        url = '/meta/training'
        params = self.param_training
        params['optimizer']='adam_test'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_loss_mode(self):
        url = '/meta/training'
        params = self.param_training
        params['loss']='MSE_test'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_early_stop_mode_mode(self):
        url = '/meta/training'
        params = self.param_training
        params['early stop']['mode']='min_test'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
        
    def test_training_wrong_early_stop_monitor_mode(self):
        url = '/meta/training'
        params = self.param_training
        params['early stop']['monitor']='monitor_test'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_learning_rate_schedule_schedule_type_mode_mode(self):
        url = '/meta/training'
        params = self.param_training
        params['learning rate schedule']['schedule type']='constant_test'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
        
    def test_training_wrong_metrics_mode(self):
        url = '/meta/training'
        params = self.param_training
        params['metrics']='accuracy'
        data =  self.connect_with_param(url, params)
        self.assertEqual(200, data['status code'], data)
    # def training 필수 검사
    
    # def metadata 파라미터 정의()
    # def metadata 타입 검사()
    # def metadata 범위 검사()
    # def metadata 모드 검사()
    # def metadata 필수 검사()
    
        
def custom_function():
    pass

if __name__ == '__main__':
    unittest.main()