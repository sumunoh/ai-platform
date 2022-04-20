import json
from collections import OrderedDict

class model_message:
  def __init__(self):
    model = OrderedDict()
    self.model = model

  def json_message(self, id, loss, metric, epoch, train_loss, train_metric, valid_loss, valid_matric):
    self.model["ID"] = id
    self.model["loss"] = loss
    self.model["metric"] = metric
    self.model["epoch"] = epoch
    self.model["train"] ={"loss":train_loss,"metric":train_metric}
    self.model["valid"] ={"loss":valid_loss,"metric":valid_matric}
    print(json.dumps(self.model, ensure_ascii=False, indent="\t") )