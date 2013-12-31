import unittest
import pickle
from pickler import Pickler

class PickleAndUnpickle(unittest.TestCase):

    def test_pickle_and_unpickle_equals_list(self):
        list1 = [1,2,3]
        picklefile = 'test.p'
        self.pickler.list_pickler(list1, picklefile)
        another_list = self.pickler.unpickler(picklefile)
        self.assertEqual(list1, another_list)

    def setUp(self):
        self.pickler = Pickler()
        
