import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("core"), '.')) + '/github/cython_learn/')

import bpy
import mycode

mylist = bpy.data.meshes[:]
mycode.call_remove_mesh_from_meshes(mylist)
