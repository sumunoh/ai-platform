from src.data.constant import confusion_matrix
from src.data.constant import loss

METRICS=[getattr(confusion_matrix, item) for item in dir(confusion_matrix) if not item.startswith("__")]

LOSS=[getattr(loss, item) for item in dir(loss) if not item.startswith("__")]