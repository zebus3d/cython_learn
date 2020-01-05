import sys, os.path
sys.path.append(os.getcwd() + '/github/cython_learn/')

import bpy
import mycode
mylist = bpy.data.meshes[:]
# without cdef:
#mycode.remove_mesh_from_meshes(mylist, 1)

# with cdef:
mycode.call_remove_mesh_from_meshes(mylist, 1)
