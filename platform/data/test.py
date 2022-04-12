from model import Model, InputLayer, OutputLayer
from dataset import Dataset
from training import Training
from earlystop import MinMaxStop
import schedule as _schedule
from metadata import Metadata

def dict_to_input_layer(data: dict):
    return InputLayer(data['size'])

def dict_to_output_layer(data: dict):
    return OutputLayer(data['size'], data['activation'])

def dict_to_model(data: dict):
    
    input_layer = dict_to_input_layer(data['input layer'])
    output_layer = dict_to_output_layer(data['output layer'])
    initializer = data['initializer']
    save_path=data['path model save']
    name = data['name']
    gpu=data['gpu']
    
    return Model(input_layer=input_layer,
                 output_layer=output_layer,
                 initializer=initializer,
                 path_model_save=save_path,
                 name=name,
                 gpu=gpu
                 )
    
def dict_to_dataset(data: dict):
    
    dataset_type = data['dataset_type']
    path_dataset = data['path_dataset']
    fold_size = data['fold size']
    fold_number = data['fold number']
    num_worker = data['num_worker']
    random_seed = data['random_seed']
    
    return Dataset(dataset_type=dataset_type,
                path_dataset=path_dataset,
                num_worker=num_worker,
                random_seed=random_seed,
                fold_size=fold_size, fold_num=fold_number)

def dict_to_earlystop(data:dict):
    return MinMaxStop(data['mode'],data['monitor'],data['min delta'],data['patience'])

def dict_to_learningrate_schedule(data:dict):
    
    if data != None:
        schedule_name=data['schedule type']
        m_name = '{}Schedule'.format(schedule_name)
    _schedule_method = getattr(_schedule, m_name)
    
    if schedule_name == 'Constant':
        return _schedule_method()
    
    elif schedule_name == 'Expotential':
        return _schedule_method(data['x'])
    
    else :
        return _schedule_method(data['multi'])

def dict_to_train(data:dict):
    
    optimizer = data['optimizer']
    loss=data['loss']
    batch_size = data['batch size']
    learning_rate=data['learning rate']
    max_epoch = data['max epoch']
    early_stop=dict_to_earlystop(data['early stop'])
    learning_rate_schedule= dict_to_learningrate_schedule(data['learning rate schedule'])
    metrics = data['metrics']
    
    return Training(
        optimizer=optimizer,
        loss=loss,
        batch_size=batch_size,
        learning_rate=learning_rate,
        max_epoch=max_epoch,
        early_stop=early_stop,
        learning_rate_schedule=learning_rate_schedule,
        metrics=metrics
    )
    
def dict_to_metadata(data:dict):
    return Metadata(model=dict_to_model(data),
                     dataset=dict_to_dataset(data),
                     training=dict_to_train(data))
    