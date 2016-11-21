import os


class Path(object):
    '''Work with os.path as an object'''

    def __init__(self, *parms, **kwargs):
        str_parms = [str(p) for p in parms]
        self.__path = os.path.join(*str_parms)

        self.__relative_to = None

        # Collect relative_to off first path parm if we can
        try:
            self.__relative_to = parms[0].__relative_to
        except AttributeError:
            self.__relative_to = None

        for k, v in kwargs.items():
            if k == 'relative_to':
                self.__relative_to = v
            else:
                raise Exception("Unknown keyword argument: s" % (k))


    def __str__(self):
        return self.__path

    def __repr__(self):
        return "%s('%s')" % (self.__class__.__name__, self.__path)


    @property
    def _compare_str(self):
        '''String for comparison.  See .__eq__()'''
        if self.__relative_to is None:
            path = str(self)
        else:
            path = os.path.join(str(self.__relative_to), str(self))

        # Normalize path seperators
        path = Path.normalize_path_sep(path)

        return path


    @staticmethod
    def normalize_path_sep(path):
        return path.replace('/', os.path.sep).replace('\\', os.path.sep)


    def __eq__(self, other):
        '''
        Paths are equal if their string values are euqal adjusted for os.sep

        So:
          - a/b/c == a\b\c
          - /a/b/c != a/b/c (even if both paths point to the same place)

        If a path has a .rel_root value, that will be combined with the
        string value before comparing.  So:

          - 'c' relative to '/a/b' == '/a/b/c' relative to None

        :param other: Another path or string
        :return:
        '''
        try:
            return other._compare_str == self._compare_str
        except AttributeError:
            a = Path.normalize_path_sep(str(other))
            return a == self._compare_str


    def __hash__(self):
        return hash(self.__path)


    def __ne__(self, other):
        return not self.__eq__(other)


    @property
    def rel_root(self):
        '''The path that this path is relative to (if relative)'''
        if self.is_relative:
            if self.__relative_to is not None:
                return self.__relative_to
            else:
                return os.path.abspath(os.curdir)
        return None


    @property
    def is_relative(self):
        if len(self.__path) > 0:
            if self.__path[0] in ('/', '\\'):
                return False
            elif self.__path[1:3] in (':\\', ':/'):
                return False
            return True
        return None


    @property
    def is_absolute(self):
        return not self.is_relative


    def make_relative_to(self, root):
        '''Create a new path object which is same path relative to this'''
        root = str(root)

        if self.is_relative:
            path = str(self.abs)
        else:
            path = str(self)

        if not path.startswith(root):
            raise ValueError("%s cannot be represented relative to %s" %(
                path, root))
        rel_path = path[len(root)+1:] # +1 to get dir sep.  Ever want otherwise?
        return Path(rel_path, relative_to=root)


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
        if self.is_relative:
            if self.__relative_to is not None:
                return Path(self.__relative_to, self.__path)
            else:
                return Path(os.path.abspath(self.__path))
        else:
            return Path(os.path.abspath(self.__path))

    @property
    def basename(self):
        return os.path.basename(self.__path)

    @property
    def parent(self):
        return Path(os.path.dirname(self.__path))


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
        return str(self.norm).split(os.sep)

    def has_ext(self, *exts):
        return self.ext.lower() in set([e.lower() for e in exts])

    @property
    def norm(self):
        return Path(os.path.normpath(self.__path))


    def join(self, *paths):
        paths = [self.__path, ] + [str(p) for p in paths]
        return Path(os.path.join(*paths), relative_to=self.__relative_to)


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
        return self.walk()


    def walk(self):
        '''
        Return all sub directories and files recursivly

        Returned paths are RelativePath
        '''
        for dirpath, dirnames, filenames in os.walk(str(self.abs)):
            for name in dirnames:
                yield Path(dirpath, name).make_relative_to(self.abs)
            for name in filenames:
                yield Path(dirpath, name).make_relative_to(self.abs)




