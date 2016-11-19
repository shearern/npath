import os

from unittest import TestCase

from npath import RelativePath

class TestRelativePath(TestCase):

    def test_rel_path(self):

        root = RelativePath('/root/path')
        child = root.join('sub_file.txt')

        self.assertEquals(str(root), os.path.normpath('.'))
        self.assertEquals(os.path.normpath(root.full_path),
                          os.path.normpath('/root/path'))

        self.assertEquals(os.path.normpath(str(child)),
                          os.path.normpath('sub_file.txt'))
        self.assertEquals(os.path.normpath(child.full_path),
                          os.path.normpath('/root/path/sub_file.txt'))
