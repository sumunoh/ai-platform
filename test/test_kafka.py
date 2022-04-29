import unittest
from src.kafka import Kafka
import json
from collections import OrderedDict

class test_kafka(unittest.TestCase):
  
    def test_epoch_message(self):
        ka = Kafka()
        a = ka.epoch_message(1111, "mse", "acc", 1, 0.3, 0.3, 0.3, 0.3)

        model = OrderedDict()
        model["ID"] = 1111
        model["loss"] = "mse"
        model["metric"] = "acc"
        model["epoch"] = 1
        model["train"] ={"loss":0.3,"metric":0.3}
        model["train"] ={"loss":0.3,"metric":0.3}
        model["valid"] ={"loss":0.3,"metric":0.3}        
        b = json.dumps(model, ensure_ascii=False, indent="\t")

        self.assertEqual(a,b)


if __name__ == '__main__':
    unittest.main()
