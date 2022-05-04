import json
from collections import OrderedDict
# import sys 
# sys.path.insert(0, '../src')
from src import dao_exception

class Kafka:
  def __init__(self):
    pass

  def epoch_message(self, uniq_id: int, loss_name: str, metric_name: str, epoch: int, train_loss: float, train_metric: float, valid_loss: float, valid_matric: float):
    int_ = [uniq_id, epoch]
    str_ = [loss_name, metric_name]
    float_ = [train_loss, train_metric, valid_loss, valid_matric] 
    
    for i in int_:
      dao_exception.dao_type("{}".format(i), i, int)
    
    for i in str_:
      dao_exception.dao_type("{}".format(i), i, str)
    
    for i in float_:
      dao_exception.dao_type("{}".format(i), i, float)
      
    for i in int_:
      dao_exception.dao_range_oneway("{}".format(i), i, 0, 'eq_n_up')

    for i in float_:
      dao_exception.dao_range_oneway("{}".format(i), i, 0, 'eq_n_up')


    model = OrderedDict()
    model["ID"] = uniq_id
    model["loss"] = loss_name
    model["metric"] = metric_name
    model["epoch"] = epoch
    model["train"] ={"loss":train_loss,"metric":train_metric}
    model["valid"] ={"loss":valid_loss,"metric":valid_matric}

    message = json.dumps(model, ensure_ascii=False, indent="\t")
    
    return message