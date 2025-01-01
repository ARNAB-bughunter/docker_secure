########################################################
# This program builds .so files from .py files
# and delete '.py', '.c' and '.pyc' files.# install cpython:
# sudo pip install cython
# Command to run build:
# python3 compile.py build_ext --inplace
########################################################

import os
from setuptools import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from pathlib import Path
from typing import List


def cythonizer(each_py:Extension):
    try:
        setup(ext_modules = cythonize(each_py,compiler_directives={
            'c_string_type': 'str',
            'c_string_encoding': 'utf8',
            'language_level': 3}))
    except Exception as e:
        print(f"Error:>>\n{e}\n\n")

def deletefiles(folder_path:str, file_type:List):
    all_files = list(map(lambda y: os.path.join(folder_path,y), filter(lambda x: os.path.isfile(os.path.join(folder_path,x)), os.listdir(folder_path))))

    req_files = list(filter(lambda file_path: os.path.splitext(file_path)[1].lower() in file_type, all_files))

    print(f"Deleting following files from {folder_path}\n{req_files}\n\n")

    for each_file in req_files:
        os.remove(each_file)



main_path = "src"

exclude_folder = ["__pycache__"]

all_py_files = []
dirs_to_check = []
for (root,_,files) in (os.walk(main_path, topdown=True)):
    if files and not set(root.split("/")) & set(exclude_folder):
        dirs_to_check.append(root)
        for file in files:
            if os.path.splitext(file)[1].lower() == '.py':
                  file = os.path.join(root,file)
                  packagename = Path(file.replace("/", ".")).resolve().stem
                  exten = Extension(packagename, [str(file)])
                  cythonizer(exten)


for each_dir in dirs_to_check:
    deletefiles(each_dir, [".c", ".py"])