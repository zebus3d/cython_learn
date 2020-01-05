import sys, os.path
sys.path.append(os.getcwd() + '/github/cython_learn/')
import bpy
import mycode
mylist = bpy.data.meshes[:]
mycode.remove_mesh_from_meshes(mylist, 1)
