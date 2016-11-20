from abc import ABCMeta, abstractmethod, abstractproperty

from . import Path
from . import RelativePath


class FileObject(object):
    __metaclass__ = ABCMeta

    FILE_OBJ_FACTORY = None # set in __init__.py

    def __init__(self, *path_parts):
        self.__path = Path(*path_parts)

    @property
    def path(self):
        return self.__path


    def __str__(self):
        return str(self.path)

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.__path)

    def __eq__(self, other):
        try:
            return self.path == other.path
        except AttributeError:
            return self.path == str(other)


    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash(self.path)


    @abstractproperty
    def is_file(self):
        '''Is this a file object'''


    @abstractproperty
    def is_dir(self):
        '''Is this a directory object'''

