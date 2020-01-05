from distutils.core import setup
from Cython.Build import cythonize

# For compile this:
# python3 setup.py build_ext --inplace

setup(
    name = 'mycode',
    ext_modules = cythonize("mycode.pyx", annotate=True)
)