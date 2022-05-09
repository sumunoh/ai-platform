import unittest
from src.data import dataset

class DatasetTest(unittest.TestCase):
    def test_init(self):
        data = dataset.Dataset('filepath', 5, 1, 2, 10, 'h5')

        self.assertTrue(True)

    def test_init_path_dataset_error(self):
        # type error
        error = None
        try:
            dataset.Dataset(-1, 5, 1, 2, 10, 'h5')
        except TypeError as e:
            error = e

        self.assertIsInstance(error, TypeError)

    def test_init_fold_size_error(self):
        # type error
        error = None
        try:
            dataset.Dataset('filepath', 0.1, 1, 2, 10, 'h5')
        except TypeError as e:
            erorr = e

        self.assertIsInstance(error, TypeError)

        # value error
        error = None
        try:
            dataset.Dataset('filepath', 0, 1, 2, 10, 'h5')
        except ValueError as e:
            error = e

        self.assertIsInstance(error, ValueError)
