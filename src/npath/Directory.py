from .Path import Path
from .RelativePath import RelativePath

from FileObject import FileObject

class Directory(FileObject):


    def make_subpaths_rel(self):
        self.__path = RelativePath(str(self.__path))


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