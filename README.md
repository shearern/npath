npath
=====

Work with os.path as Path objects.

It seems like 50% of my development is working with file paths.
This library is intended to make much of that path woprk a bit cleaner
but baking some of my common usage patterns of
[os.walk](https://docs.python.org/2/library/os.html) right into the 
Path objects.  I'll also change a few of the names to ones that
I can remember easier.

Basic Usage
-----------

**Path** class is used to manipulate paths
 
**File** and **Directory** are used to work with the file system
objects.

Change Log
----------

**v1.0.0**

  - Basic completion with some tests.