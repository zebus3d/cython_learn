from distutils.core import setup
from Cython.Build import cythonize

# For compile this:
# python3 setup.py build_ext --inplace

setup(
    name = 'core',
    ext_modules = cythonize("code.pyx", annotate=True)
)