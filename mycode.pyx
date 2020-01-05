import cython

@cython.locals(meshes = list)
cdef remove_mesh_from_meshes(meshes):
    for mesh in meshes:
        if mesh.users < 0:
            print("delete: ", mesh)
            meshes.remove(mesh)

def call_remove_mesh_from_meshes(meshes = list):
    print("remove_mesh_from_meshes called!")
    remove_mesh_from_meshes(meshes)

@cython.locals(objects = list)
cdef remove_objects(objets):
    for ob in objets:
        if ob.users < 0:
            print("delete: ", ob)
            objets.remove(ob)

def call_remove_bjects(objects = list):
    print("remove_objects called!")
    remove_objects(objects)