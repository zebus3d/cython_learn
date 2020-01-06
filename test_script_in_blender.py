import bpy
from datetime import datetime

#import sys, os.path
#sys.path.append(os.getcwd() + '/github/cython_learn/')
from . import mycode

start = datetime.now()

users = 0 # <-- if have 0 users, delete this orphan data mesh

mylist = bpy.data.meshes[:]
# without cdef:
#mycode.remove_mesh_from_meshes(mylist, users)

# with cdef:
mycode.call_remove_mesh_from_meshes(mylist, users)

print("total time: ", datetime.now() - start)
