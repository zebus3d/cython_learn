import cython

@cython.locals(
    os_name=str,
    os_arch=str,
    matriz=list,
    size_x=cython.int
)
def remove_mesh_from_meshes(meshes):
    for mesh in meshes:
        if mesh.users < 0:
            print("delete: ", mesh)
            meshes.remove(mesh)

@cython.locals(
    os_name=str,
    os_arch=str,
    matriz=list,
    size_x=cython.int
)
def remove_mesh_from_objects(objets):
    for ob in objets:
        if ob.users < 0:
            print("delete: ", ob)
            objets.remove(ob)