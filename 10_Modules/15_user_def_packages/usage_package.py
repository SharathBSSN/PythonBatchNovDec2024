import os
import sys

# import package.module1
# import package.module2
# import package.module3

print(os.getcwd())

print(os.listdir())


# paths it will check for imports
# for each_path in sys.path:
#     print(each_path)

# adding the path
# sys.path.insert(0, "package") #priority search add at beggining->0
# sys.path.append("package") # addes to the path list at the end
"""
# added custom paths
    # /package

current directory 
    # /workspaces/PythonBatchNovDec2024/10_modules/user_defined_packages

    /workspaces/PythonBatchNovDec2024/10_Modules/15_user_def_packages

builtin modules    
    # /usr/local/python/3.12.1/lib/python312.zip
    # /usr/local/python/3.12.1/lib/python3.12
    # /usr/local/python/3.12.1/lib/python3.12/lib-dynload

    /opt/conda/lib/python312.zip
    /opt/conda/lib/python3.12
    /opt/conda/lib/python3.12/lib-dynload

installed modules    
    # /workspaces/PythonBatchNovDec2024/.venv/lib/python3.12/site-packages

    /home/codespace/.local/lib/python3.12/site-packages
    /opt/conda/lib/python3.12/site-packages

"""

# importing a single script --- module
# import module1


# importing entire folder of scripts -- package
import package
print(package)
print(dir(package))


print(dir(package.module1 ))

package.module1.hello_world()
package.module2.hello_world()

try:
    package.module3.hello_world()
except AttributeError as ae:
    print(ae)