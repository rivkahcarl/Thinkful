class Pickler(object):

    def list_pickler(self, list1, picklefile):
        list1 = [1, 2, 3]
        picklefile = open('test.p', 'wb')
        pickle.dump(list1, output)
        picklefile.close()


    def unpickler(self, picklefile1):
        picklefile = open(picklefile, 'rb')
        list1 = pickle.load(picklefile)
        picklefile.close()
        return list1
        