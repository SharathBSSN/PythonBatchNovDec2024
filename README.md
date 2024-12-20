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

        Ex: Pushing changes from class01 -> mail
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