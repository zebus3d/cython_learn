# Learning basic Cython
Test for lean cython with blender.

# To see which files are most worth optimizing:
$ python3 -m cProfile -s time main.py

# For compile on the fly:
$ cythonize --inplace --annotate archivo.py

# Normal Compilation:
$ python3 setup.py build_ext --inplace

In Unix use ".so" files (in windows ".dll" i believe) these files are imported into your normal python code. 
