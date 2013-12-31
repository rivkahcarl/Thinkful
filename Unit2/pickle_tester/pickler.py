import sys
import os
import pickle
import unittest

def list_pickler():
    list1 = [1, 2, 3]
    output = open('test.p', 'wb')
    pickle.dump(list1, output)
    output.close()


def unpickler():
    picklefile = open('test.p', 'rb')
    list1 = pickle.load(picklefile)
    picklefile.close()