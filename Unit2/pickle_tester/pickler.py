import pickle
class Pickler(object):

    def list_pickler(self, list1, picklefile):
        picklefile2 = open(picklefile, 'wb')
        pickle.dump(list1, picklefile2)
        picklefile2.close()


    def unpickler(self, picklefile1):
        picklefile = open(picklefile1, 'rb')
        list1 = pickle.load(picklefile)
        picklefile.close()
        return list1
        