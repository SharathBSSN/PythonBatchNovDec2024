# packag3

documentiuaon about the package3

## Usage 

## edge cases

## explanation
        .
        ├── README.md
        ├── __init__.py
        ├── __pycache__   -------------------------------------> BYTECODE
        │   ├── __init__.cpython-312.pyc
        │   ├── calc.cpython-312.pyc
        │   └── operations.cpython-312.pyc
        ├── build ----------------------------------------------> Consists of all the jobs to create the packages
        │   └── bdist.linux-x86_64
        ├── calc.html
        ├── calc.py
        ├── dist
        │   ├── package3-0.1.0-py3-none-any.whl-----------------> Pre-built and ready-to-install package format
        │   └── package3-0.1.0.tar.gz --------------------------> Allow users to build and install the package manually
        ├── operations.py
        ├── package3.egg-info ----------------------------------> Consists all the dependencies, meta from README, setup.py, etc
        │   ├── PKG-INFO
        │   ├── SOURCES.txt
        │   ├── dependency_links.txt
        │   └── top_level.txt
        ├── setup.py
        └── usage.py
