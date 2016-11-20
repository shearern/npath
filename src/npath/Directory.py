from .Path import Path
from .RelativePath import RelativePath

from FileObject import FileObject

class Directory(FileObject):


    def make_subpaths_rel(self):
        self.__path = RelativePath(str(self.__path))


    @property
    def rel_root_path(self):
        '''Return path as a RelativePath rooted here'''
        return RelativePath(root_path = str(self.path))


    @property
    def is_file(self):
        return False


    @property
    def is_dir(self):
        return True


    @property
    def parent(self):
        return self.FILE_OBJ_FACTORY(self.path.parent)


    @property
    def files(self):
        for path in self.path.files:
            yield self.FILE_OBJ_FACTORY(path)


    @property
    def dirs(self):
        for path in self.path.dirs:
            yield self.FILE_OBJ_FACTORY(path)


    @property
    def all(self):
        for o in self.files:
            yield o
        for o in self.dirs:
            yield o


    @property
    def walk(self):
        for path in self.path.walk():
            yield self.FILE_OBJ_FACTORY(path)


    def find(self, files=None, dirs=None):
        for child in self.walk():
            if child.is_file:
                if files is None or files is True:
                    yield child
            elif child.is_dir:
                if dirs is None or dirs is True:
                    yield child
