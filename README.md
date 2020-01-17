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
$ python3 setup.py build_ext --inplace 

In Unix use ".so" files, in windows ".pyd", these files are imported into your normal python code. 

# For compile in Windows 10:
You need "MS Windows SDK for Windows 7 and .NET Framework 4", and "Visual Studio Build Tools 2019".
then open the Developer Command Pront vor VS 2019 and compile from there. It is not recommended to use MinGW.

# Automatic convert .pyx to .so compiled (Because writing a setup.py each time is painful):
$ sudo pip3 install easycython

$ easycython voronoi.pyx
