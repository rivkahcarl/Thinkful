import unittest
import pickle
from pickler import list_pickler, unpickler

class PickleAndUnpickle(unittest.TestCase):

    def test_pickle_and_unpickle_equals_list(self):
        my_list = self.list_pickler.list1()
        another_list = self.unpickler.list1()
        self.assertEqual(my_list, another_list)
