import  sys

sys.dont_write_bytecode = True #Does not create the Byte Code -> __pycache__ will not be created


import os

print(os.listdir())


import my_script

print(dir(my_script))


print(f""" 
    {my_script.GREETINGS =}

    {my_script.__name__ =}
    {my_script.__doc__ =}
    {my_script.hello_world =}
    {my_script.hello_world.__doc__ =}

""")

print(callable(my_script.GREETINGS))  # False
print(callable(my_script.hello_world))  # True

my_script.hello_world()