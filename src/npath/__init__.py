from Path import Path

from FileObject import FileObject
from File import File
from Directory import Directory
from InvalidFileObject import InvalidFileObject

def file_object_factory(*path_parts):
    path = Path(*path_parts)
    if path.is_file:
        return File(path)
    elif path.is_dir:
        return Directory(path)
    else:
        return InvalidFileObject(path)

FileObject.FILE_OBJ_FACTORY = file_object_factory