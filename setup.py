#!/usr/bin/env python

import numpy
from setuptools import setup
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

ext_modules = [Extension("pyxc/evalxc",
                         sources=["pyxc/evalxc.pyx", "pyxc/c_evalxc.c"],
                         include_dirs=[numpy.get_include()],
                         libraries=["xc"],)]

setup(name='pyxc',
      version='0.1',
      description='python wrapper to libXC',
      url='http://github.com/fuulish/pyXC.git',
      author='Frank Uhlig',
      author_email='uhlig.frank@gmail.com',
      license='GPLv3',
      packages=['pyxc'],
      zip_safe=False,
      ext_modules = cythonize(ext_modules),
      )
