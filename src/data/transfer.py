from src.data.model import Model, InputLayer, OutputLayer
from src.data.dataset import Dataset
from src.data.training import Training
from src.data.earlystop import MinMaxStop
from src.data import schedule as _schedule
from src.data.metadata import Metadata

def dict_to_input_layer(data: dict):
    return InputLayer(data['size'])

def dict_to_output_layer(data: dict):
    return OutputLayer(data['size'], data['activation'])

def dict_to_model(data: dict):
    param_dict = {"input layer":"input_layer",
                  "output layer":"output_layer",
                  "path" :"path",
                  "layer":"layer",
                  "path model save":"path_model_save",
                  "initializer":"initializer",
                  "name":"name",
                  "gpu":"gpu"}
    
    rekey_data=dict((param_dict[key], value) for (key, value) in data.items())
    
    rekey_data['input_layer'] = dict_to_input_layer(rekey_data['input_layer'])

    rekey_data['output_layer'] = dict_to_output_layer(rekey_data['output_layer'])
    
    return Model(**rekey_data)
    
def dict_to_dataset(data: dict):
    #ok
    param_dict = {"dataset type":"dataset_type",
                  "path dataset":"path_dataset",
                  "fold size" :"fold_size",
                  "num worker":"num_worker",
                  "fold number":"fold_number",
                  "random seed":"random_seed"}

    rekey_data=dict((param_dict[key], value) for (key, value) in data.items())
    
    return Dataset(**rekey_data)

def dict_to_earlystop(data:dict):
    return MinMaxStop(data['mode'],data['monitor'],data['min delta'],data['patience'])

def dict_to_learningrate_schedule(data:dict):
    schedule_name=data['schedule type']
    
    # if data != None:
    #     m_name = '{}Schedule'.format(schedule_name)
    # _schedule_method = getattr(_schedule, m_name)
    
    if schedule_name == 'Constant':
        return _schedule.ConstantSchedule()
    
    elif schedule_name == 'Expotential':
        return _schedule.ExpotentialSchedule(data['x'])
    
    else :
        return _schedule.MulytiplySchedule(data['multi'])

def dict_to_training(data:dict):
    param_dict = {"optimizer":"optimizer",
                  "loss":"loss",
                  "batch size" :"batch_size",
                  "learning rate":"learning_rate",
                  "max epoch":"max_epoch",
                  "early stop":"early_stop",
                  "learning rate schedule":"learning_rate_schedule",
                  "metrics":"metrics"}

    rekey_data=dict((param_dict[key], value) for (key, value) in data.items())
    rekey_data['early_stop']=dict_to_earlystop(data['early stop'])
    rekey_data['learning_rate_schedule']= dict_to_learningrate_schedule(data['learning rate schedule'])
    
    return Training(**rekey_data)
    
def dict_to_metadata(data:dict):
    return Metadata(model=dict_to_model(data['model']),
                     dataset=dict_to_dataset(data['dataset']),
                     training=dict_to_training(data['training']))
    