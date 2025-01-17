# PythonBatchNovDec2024

This repository is developed to learn and understnd Python and its real-corporate level implementatins with the use of Git, GitHub and GitHub-Codespace.

## Git Commands

To make a clone of any given repo, ignore for codespace  [codespace allows to directly work on your given reposiory space]

    git clone <url>

To List all branches

    git branch

    git branch <branchName>  [Creates a new branch]

To switch to or check out into anothe branch

    git checkout <branchName>

    git checkout -b <branchName>  [Creates a new branch and checks it out to current working direcory]

To see modified files in local directory

    git status

To see changes made on file

    git diff <fileName> [changed but not staged]

    git diff --staged [staged but not commmited]

To add/stage the changes

    git add <fileName>

To commit the changes

    git commit -m "commit message"

To push the commited changes

    git push origin <sourceBranch>

        Ex: Pushing changes from class01 -> main
        git push origin class01

### Daily 

These are the list of instructions or recommended practices that allows one to be on page with repo, identifying any uncommited changes.

To check current working directory, bracnch

    git status

To check out to main branch

    git checkout main

To get the latest changes

    git pull origin main

To create new branch 

    git checkout -b <branchName>


## Virtual Environment

    Isolated environment 

    why needed
        - same system, multiple projects
            - different python versions 
            - same python verison, but differenet module versions

    How to create Virtual Environment 
        - Virtualenv
        - venv
        - pipenv
        - poetry 
        - uv

    Using Virtualenv
        
        Install
            pip install virtualenv
        
        create virtual environment
            python -m virtualenv .venv
        
        activate virtual environment
            linux
                source .venv/bin/activate

            windows
                .venv/script/activate

        Using Poetry

            Install
                pip install -U pip
                pip install poetry

            Initialize
                python -m poetry init

            Create a virtual env
                python -m poetry shell

            Add Dependencies
                pip install poetry
                poetry add pandas    



## What I have learnt so far...

Installation and Initialization of Git, GitHub, Codespace, Python

Git commands, markdown(.md) syntax, daily activity and usage

Intro to Python

Class02

    PEP 8 GuideLines,
    Shebang Line,
    Dynamic Typing,
    Indentation and best parctices,
    Print Syntax and Print Function,
    Script vs Interactive mode
    JupyterNotebooks (.ipynb) usage
    ASCII and UNICODE

Class03

    Keywords, Indentifiers
    Indentifier Casing
    Comments, DocString
    Semicolan Operators

    Arthmetic Operations -> +,-,*,/,//,%,**
    Arthmetic Functions  -> divmod(), pow()



Class04

    abs(), complex numbers
    type conversion
    operator precedence
    
Class05

    String Operations - Basics, use of quotes, len()
    String Indexing
    String Sclicing 

Class06

    String Sclicing, String Reversal
    String Attributes

    
Class07

    String Attributes

Class08

    String Formatting: Old and New
    f-strings, unicode strings

Class09

    Byte Operations, Usage of help()
    pydoc
    Relational Operations
    Logical Operations

Class10

    Boolean Operations
    Bitwise Operations
    Identity Operations
    Dual Memory management Strategy
    range() function
    Conditional Operations

Class11

    Structural Pattern Matching
    Loops: for & while, break, continue, pass, sys.exit

Class12

    Walrus Operator
    Exceptions Hierarchy
    Different types of errors, error vs exception and exception groups
    Handling single and multiple exceptions
    raising exceptions
    asserts
    traceback
    exception Groups
    warnings

Class13

    Debugging
    Importance of logical errors
    Debugging with pydevd
    Debugging with pdb, ipdb
    breakpoint() function
    PYTHONBREAKPOINT environment variable usage
    post analyses of executed script

Class14

    Collections
    Lists

Class15

    Copy Problem - shallow copy vs deepcopy
    Tuples & namedtuples
    Immutability & unpacking
    Sets- attributes, operations

class16

    fronzensets
    Dictionaries
        zip() function
        workaround for switch case
    Comprehensions
    Working with Iterables - sum(), max(), min()

class17

    Functions
    Functions with & without arguments, keyword arguments
    Functions with Different return types and unpacking
    Functions with with Default arguments
    variadic functions : variable arguments and variable keyword arguments
    Functions with keyword only arguments
    Scoping: Global vs Local
        call by reference
        call by value

class18

    Partial Functions
    Anonymous(Lambda) Functions
    Higher order functions: map(), filter(), functool.reduce()
    Recursions and recursions limit


class19

    inner functions
    closures
    Decorator Design Pattern
    Necessity
    function Decorator
    Practical Examples
    syntactic sugar for decorators
    multiple decorators on same function
    decorators with arguments
    functools - wrap, lru_cache
    class decorator


class20

    Iterables, Iterators, Generators and co-routines
    Iterables
        different ways of extracting values from iterables
    Iterators
        iter() protocol
        itertools module

class21

    Generators
        yield vs return
        function vs Generator
        Generator pipelining
        Generator Expression

class22 

    Coroutine
        Generator vs Coroutine
        coroutine pipelining
    Modules
        Basic Modules
            - math, sys, argparse

class23 

        os, pathlib, psutil
        
class24 

    shutil, subprocess, getpass
    time related
        - time, datetime, pytz, timeit, calendar
    others
        - random, collections, atexit, contextlib, base64

class25 

    creating user-defined module and package
        packaging
        creating the wheel files, tar files
        publishing with twine
        egg files
    File Operations
        flat files

class26

    Non-flat files 
        pickle 
        shelve 
        xml 
        csv

class26 

        windows local setup
        poetry installation
        Troubleshooting experince
        csv
        dat
        tsv