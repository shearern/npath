
from .Path import Path
from .RelativePath import RelativePath

from .FileObject import FileObject

class InvalidFileObject(FileObject):
    '''When we get a path that doesn't actually point to areadl object'''


    @property
    def is_file(self):
        return False


    @property
    def is_dir(self):
        return False
