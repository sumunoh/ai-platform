import json
from collections import OrderedDict

class Kafka:
  def __init__(self):
    pass

  def epoch_message(self, id: int, loss_name: str, metric_name: str, epoch: int, train_loss: float, train_metric: float, valid_loss: float, valid_matric: float):
    model = OrderedDict()
    model["ID"] = id
    model["loss"] = loss_name
    model["metric"] = metric_name
    model["epoch"] = epoch
    model["train"] ={"loss":train_loss,"metric":train_metric}
    model["valid"] ={"loss":valid_loss,"metric":valid_matric}

    # print(json.dumps(model, ensure_ascii=False, indent="\t"))