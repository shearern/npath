npath
=====

Work with os.path as Path objects.

It seems like 50% of my development time is spent working with file paths.
This library is intended to make much of that path work a bit cleaner
by baking some of my common usage patterns of
[os.path](https://docs.python.org/2/library/os.path.html) right into the 
Path objects.  I'll also change a few of the names to ones that
I can remember easier.


Key Classes
-----------

**Path** class is used to manipulate paths
 
**File** and **Directory** are used to work with the file system
objects.


Basic Usage
-----------

Setting a path value 

    from npath import Path
    path = Path('path/to/file')
    
    print(str(path))
    
    
Path Joining

    a = Path('/usr/share/man')
    b = Path('en/man1/whatis.1.gz')
    
    a.join(b) == Path('/usr/share/man/en/man1/whatis.1.gz')
    
    # Also:
    a.join('en/man1/whatis.1.gz') == Path('/usr/share/man/en/man1/whatis.1.gz')
    
    
Listing the files in a directory

    from npath import File, Directory
    
    d = Direcotry('/usr/share/man')
    
    for file in d.files:
        print(str(file))


Listing the directories in a directory

    from npath import File, Directory
    
    d = Direcotry('/usr/share/man')
    
    for a_dir in d.dirs:
        print(str(a_dir))


Listing the files and directories in a directory

    from npath import File, Directory
    
    d = Direcotry('/usr/share/man')
    
    for fobj in d.all:
        print(str(fobj))


Recursivly walk over all sub files and sub directroies of a path

    for fobj in Directory('/usr/share/man').walk():
        if fobj.is_file:
            print ("FILE: %s" % (fobj))
        elif fobj.is_dir:
            print ("DIR:  %s" % (fobj))


Opening a file in a directory

    d = Direcotry('/home/auser')
    fh = d.join('my_file.txt').open('w')
    fh.write("...")
    fh.close()


Change Log
----------

**v1.0.0**

  - Basic completion with some tests.