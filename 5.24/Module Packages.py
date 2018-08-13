# an import can name a directory path. A directory of
# Python code is said to be a package, so such imports are known as package imports.

import dir1.dir2.test

# __init__ serves primarily as a hook for performing initialization
# steps required by the package

# these files are a
# natural place to put code to initialize the state required by files in a package. For
# instance, a package might use its initialization file to create required data files, open
# connections to databases, and so on.

from imp import reload # from needed in 3.X only
import dir1.dir2.mod

reload(dir1)
reload(dir1.dir2)

print(dir1.x)
print(dir1.dir2.y)
print(dir1.dir2.mod.z)

from dir1.dir2.mod import z
print(z) # shorter

import dir1.dir2.mod as mod # shorter name

#use of packages is for being descriptive
import database.client.utilities

#skipping rest, come back if future needs
