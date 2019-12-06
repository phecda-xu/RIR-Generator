from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import os.path
import numpy as np

# python3 setup.py build_ext --inplace

extensions = [
	Extension("*", ["pyrirgen.pyx"],
		include_dirs=[
			os.path.abspath("."),
		],
		library_dirs=[os.path.abspath(".")],
		libraries=["rirgen"],
		language='c++'
	),
]

setup(
	name = 'pyrirgen',
	ata_files = [('', ['librirgen.so'])],
	ext_modules=cythonize(extensions, compiler_directives = {
		'language_level': 3, # Python 3
		'embedsignature': True, # add method signature to docstrings, thus tools can display it after compilation
		'c_string_encoding': 'default',
		'c_string_type': 'str',
	}),
)
