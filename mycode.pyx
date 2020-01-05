import cython
import bpy

@cython.locals(meshes = list, fake_users = cython.int)
def remove_mesh_from_meshes(meshes, fake_users):
    print("Clear orphan meshes...")
    for mesh in meshes:
        if mesh.users < fake_users:
            print("Delete: ", mesh.name, " now")
            bpy.data.meshes.remove(mesh)
