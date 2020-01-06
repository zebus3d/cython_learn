# Learning basic Cython
Test for lean cython with blender.

# Install dependencies:
$ pip install cython

# To see which files are most worth optimizing:
$ python3 -m cProfile -s time main.py

$ sudo apt install build-essential python3-dev 

# You must have installed in your system the same python version that uses blender, exactly the same.  
In my Linux Mint 19.3 Tricia:

Download python 3.7.4

cd folder

$ sudo apt install zlib1g-dev libffi-dev libssl-dev

$ sudo apt purge pytho3-pip

$ ./configure --with-ssl

$ make -j 2

$ sudo make install

$ sudo chown $USER:$USER -R $HOME/.cache


Note: in pycharm put existent enviroment: /your/path/Python-3.7.4/Python/

# For compile on the fly:
$ cythonize --inplace --annotate archivo.py

# Normal Compilation:
$ python3 setup.py build_ext --inplace or

$ python3 setup.py build_ext --inplace && mv mycode.cpython-37m-x86_64-linux-gnu.so mycode.so

In Unix use ".so" files (in windows ".dll" i believe) these files are imported into your normal python code. 
