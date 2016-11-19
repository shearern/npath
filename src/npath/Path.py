import os


class Path(object):
    '''Work with os.path as an object'''

    def __init__(self, *parms):
        parms = [str(p) for p in parms]
        self.__path = os.path.join(*parms)


    def __str__(self):
        return self.__path

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.__path)

    @property
    def is_file(self):
        return os.path.isfile(self.__path)


    def open(self, mode):
        return open(self.__path, mode)