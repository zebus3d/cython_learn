# cython_learn
Quickly cython test

# Para ver que archivos merecen mas la pena optimizar:
$ python -m cProfile -s time main.py

# Para compilar on the fly:
$ cythonize --inplace --annotate archivo.py

# Compilar normal:
$ python3 setup.py build_ext --inplace

El .so en unix es la librería (creo que en windows sera un .dll) que se importa en el script python norma. 
