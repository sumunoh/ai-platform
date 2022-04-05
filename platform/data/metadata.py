import schedule as _schedule
import dataset as _dataset

class Metadata:
    def __init__(self) -> None:
        self.dataset : _dataset.Dataset = None
        self.schedule : _schedule.LearningSchedule = None


    def __iter__(self):
        yield 'dataset', dict(self.dataset)
        yield 'schedule', dict(self.schedule)
