# You’re always in a module in Python. There’s no way to write code that doesn’t
# live in some module

#  even code typed at the interactive prompt really goes in a built-in module called  __main__;

#  The only things a module should share
# with the outside world are the tools it uses, and the tools it defines.
# minimize the global variables

# As a special case, you can prefix names with a single underscore (e.g., _X) to prevent
# them from being copied out when a client imports a module’s names with a from * statement

# _b and _d in unders
from unders import *
print(a, c)

# just import will see _b
import unders
print(unders._b)

from alls import *  # Load __all__ names only
print(a, _c)

# put __all__ = [a, _c] to define what is imported with a * statement

# from __future__ import featurename
# put this code to update code like generator, print, etc
# it will replace current code with changes
# list is seen with dir
#takes the form
# from __future__ import functionname
#first statement

import __future__
print(dir(__future__))

#  each module has a built-in attribute called __name__

# • If the file is being run as a top-level program file, __name__ is set to the string
# "__main__" when it starts.
# • If the file is being imported instead, __name__ is set to the module’s name as known
# by its clients.

import runme

# ^ in this file, does not run the def, in runme it does run the def

# The upshot is that a module can test its own __name__ to determine whether it’s being
# run or imported.

# In effect, a module’s __name__ variable serves as a usage mode flag, allowing its code to
# be leveraged as both an importable library and a top-level script.

# import sys
#
#         if len(sys.argv) == 1:
#             selftest()

# checks if number of arguments is 0
import sys
print(sys.path)
sys.path.append('/home/randy/venv/bin/')
print(sys.path)
# Once you’ve made such a change, it will impact all future imports anywhere while a
# Python program runs, as all importers share the same single sys.path list (there’s only
# one copy of a given module in memory during a program’s run—that’s why reload
# exists).

# sys.path settings endure for only as long as the Python session
# or program (technically, process) that made them runs; they are not retained after
# Python exits.

# import modulename as name # And use name, not modulename
# using as changes the name of the imported file

# from dir1.dir2.mod import func as modfunc # Rename to make unique if needed

# x = 'string'
# import x
# Here, Python will try to import a file x.py, not the string module

#to get around this

modname = 'alls'
exec('import ' + modname) # Run a string of code
print(alls) # Imported in this namespace

# exec compiles a string of code and passes it to the Python interpreter to be executed

modname = 'alls'
string = __import__(modname)
print(alls)
#faster

#go back to gotchas
