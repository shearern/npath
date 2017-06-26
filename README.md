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


|                                            | os                                        | npath                                                        |
|--------------------------------------------|-------------------------------------------|--------------------------------------------------------------|
| Base portion of path                       | os.path.basename('my/path')               | Path('my/path').basename                                     |
| Parent portion of path                     | N/A                                       | Path('my/path/to').parent == Path('my/path')                 |
| Absolute path                              | os.path.abspath('my/path')                | Path('my/path').abs                                          |
| Normalized path                            | os.path.normpath('my/path')               | Path('my/path').norm                                         |
| Get file extension                         | os.path.splitext('my/path/myfile.txt')[0] | Path('my/path/myfile.txt') Note: Doesn't include leading '.' |
| Does the path point to an existing object? | os.path.exists('my/path')                 | Path('my/path').exists                                       |
| Does path point to a file?                 | os.path.isfile('my/path')                 | Path('my/path').is_file                                      |
| Does path point to a directory?            | os.path.isdir('my/path')                  | Path('my/path').is_dir                                       |
| Does path point to a link?                 | os.path.islink('my/path')                 | Path('my/path').is_link                                      |
|                                            |                                           |                                                              |
| Get file size                              | os.path.getsize('my/path')                | File('my/path').size                                         |
| Get file MD5 sum                           | Use hashlib                               | File('my/path').md5                                          |

Change Log
----------

**v1.0.0**

  - Basic completion with some tests.