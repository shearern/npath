import os

from .Path import Path

class RelativePath(Path):
    '''A path which is anchored at a specific parent path'''

    def __init__(self, root_path, rel_path=None):
        if rel_path is None:
            super(RelativePath, self).__init__(root_path)
        else:
            super(RelativePath, self).__init__(root_path, rel_path)
        self.__root = root_path
        self.__rel_path = rel_path


    @property
    def full_path(self):
        if self.__rel_path is None:
            return self.__root
        else:
            return os.path.join(self.__root, self.__rel_path)


    def __str__(self):
        if self.__rel_path is None:
            return '.'
        return self.__rel_path


    def __repr__(self):
        if self.__rel_path is None:
            return "RelativePath('%s', None)" % (self.__root)
        return "RelativePath('%s', '%s')" % (self.__root, self.__rel_path)


    def _new_path(self, path):
        if not path.startswith(self.__root):
            return Path(path)
        else:
            return RelativePath(self.__root, path[len(self.__root):].lstrip('/').lstrip('\\'))


    def join(self, *paths):
        paths = [self.__root, ] + [str(p) for p in paths]
        return self._new_path(os.path.join(*paths))





