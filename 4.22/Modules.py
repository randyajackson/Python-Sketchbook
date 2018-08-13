# In short, modules provide an easy way to organize components into a system by serving
# as self-contained packages of variables known as namespaces.

# For all but the simplest scripts, your programs will take the form of multifile systems

# The top-level (a.k.a. script) file contains the main flow of control
# of your program

# imports
# 1. Find the module’s file.
# 2. Compile it to byte code (if needed).
# 3. Run the module’s code to build the objects it defines.

# Byte Code Files: __pycache__ in Python 3.2+
# it will try to save byte code in a file in order to skip the
# compile step next time around.

# In Python 3.1 and earlier (including all of Python 2.X)
# Byte code is stored in files in the same directory as the corresponding source files,
# normally with the filename extension .pyc

# In Python 3.2 and later
# Byte code is instead stored in files in a subdirectory named __pycache__, which
# Python creates if needed, and which is located in the directory containing the corresponding
# source files

# how import finds:
# 1. The home directory of the program // directory of the .py file

# 2. PYTHONPATH directories (if set) // list of user-defined and platform-specific
# names of directories that contain Python code files

# 3. Standard library directories // directories where the standard library
# modules are installed on your machine

# 4. The contents of any .pth files (if present)

# 5. The site-packages home of third-party extensions

# using pythonpath
# Or you might instead create a text file called C:\Python33\pydirs.pth, which looks like
# this:
# c:\pycode\utilities
# d:\pycode\package1

# >>> import sys
# >>> sys.path
# ['', 'C:\\code', 'C:\\Windows\\system32\\python33.zip', 'C:\\Python33\\DLLs',
# 'C:\\Python33\\lib', 'C:\\Python33', 'C:\\Users\\mark',
# 'C:\\Python33\\lib\\site-packages']

#  some programs really do need to change sys.path. Scripts that run
# on web servers, for example, often run as the user “nobody” to limit machine access.
# Because such scripts cannot usually depend on “nobody” to have set PYTHONPATH in any
# particular way, they often set sys.path manually to include required source directories,
# prior to running any import statements. A sys.path.append or sys.path.insert will
# often suffice, though will endure for a single program run only.

# For example, an import statement of the form import b might today load or resolve to:
# • A source code file named b.py
# • A byte code file named b.pyc
# • An optimized byte code file named b.pyo (a less common format)
# • A directory named b, for package imports (described in Chapter 24)
# • A compiled extension module, coded in C, C++, or another language, and dynamically
# linked when imported (e.g., b.so on Linux, or b.dll or b.pyd on Cygwin
# and Windows)
# • A compiled built-in module coded in C and statically linked into Python
# • A ZIP file component that is automatically extracted when imported
# • An in-memory image, for frozen executables
# • A Java class, in the Jython version of Python
# • A .NET component, in the IronPython version of Python

#  import hooks. These hooks can be used to make
# imports do various useful things, such as loading files from archives, performing decryption,
# and so on.

# Systems that use distutils generally come with a setup.py script, which is run to install
# them; this script imports and uses distutils modules to place such systems in a directory
# that is automatically part of the module search path (usually in the Lib\site-packages
# subdirectory of the Python install tree, wherever that resides on the target machine).


