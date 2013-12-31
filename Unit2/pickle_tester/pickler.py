class pickler(object):

    def list_pickler(self, list1):
        list1 = [1, 2, 3]
        output = open('test.p', 'wb')
        pickle.dump(list1, output)
        output.close()


    def unpickler(self, list1):
        picklefile = open('test.p', 'rb')
        list1 = pickle.load(picklefile)
        picklefile.close()