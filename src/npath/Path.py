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

    def __eq__(self, other):
        self_path = self.norm

        try:
            other_path = other.norm
        except AttributeError:
            other_path = Path(str(other)).norm

        return self_path.rstrip(os.path.sep) == other_path.rstrip(os.path.sep)


    def __hash__(self):
        return hash(self.__path)


    def __ne__(self, other):
        return not self.__eq__(other)


    def _new_path(self, path):
        return Path(path)

    @property
    def exists(self):
        return os.path.exists(self.__path)

    @property
    def is_file(self):
        return os.path.isfile(self.__path)

    @property
    def is_dir(self):
        return os.path.isdir(self.__path)

    @property
    def is_link(self):
        return os.path.islink(self.__path)


    @property
    def abs(self):
        return os.path.abspath(self.__path)


    @property
    def basename(self):
        return os.path.basename(self.__path)

    @property
    def parent(self):
        return self._new_path(os.path.dirname(self.__path))


    @property
    def splitext(self):
        prefix, ext = os.path.splitext(self.__path)
        if ext is not None and ext[0] == '.':
            ext = ext[1:]
        return prefix, ext

    @property
    def prefix(self):
        return self.splitext[0]

    @property
    def ext(self):
        return self.splitext[1]

    def split(self):
        return self.norm.split(os.sep)

    def has_ext(self, *exts):
        return self.ext.lower() in set([e.lower() for e in exts])

    @property
    def norm(self):
        return os.path.normpath(self.__path)


    def join(self, *paths):
        paths = [self.__path, ] + [str(p) for p in paths]
        return self._new_path(os.path.join(*paths))


    @property
    def all(self):
        for p in self.dirs:
            yield p
        for p in self.files:
            yield p


    def list_dir(self):
        return os.listdir(self.__path)

    def samefile(self, other):
        try:
            return os.path.samefile(self.__path, str(other))
        except AttributeError:
            raise AttributeError("os.path.samefile() only available for Unix")

    @property
    def dirs(self):
        for name in self.list_dir():
            child = self.join(name)
            if child.is_dir:
                yield child


    @property
    def files(self):
        for name in self.list_dir():
            child = self.join(name)
            if child.is_file:
                yield child


    def find(self):
        for dirpath, dirnames, filenames in os.walk(self.__path):
            for name in dirnames:
                yield self._new_path(os.path.join(dirpath, name))
            for name in filenames:
                yield self._new_path(os.path.join(dirpath, name))


    def walk(self):
        return self.find()




