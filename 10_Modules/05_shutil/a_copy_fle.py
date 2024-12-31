"""
Purpose: To copy a file from one directory, to another

──────────────────  ───────────────  ──────────────────  ────────────── ───────────
     Function       Copies metadata  Copies permissions  Can use buffer Dest dir OK
──────────────────  ───────────────  ──────────────────  ────────────── ───────────
shutil.copy               No                 Yes             No             Yes
shutil.copyfile           No                 No              No             No
shutil.copy2              Yes                Yes             No             Yes
shutil.copyfileobj        No                 No              Yes            No
──────────────────  ───────────────  ──────────────────  ────────────── ───────────

shutil.move - To move file from one place to another

"""
import os
import shutil

# print(dir(shutil))


'''
 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat',
 'copytree', 'disk_usage', 'errno', 'fnmatch', 'get_archive_formats'
 'get_terminal_size', 'get_unpack_formats', 'ignore_patterns', 'make_archive', 
 'move', 'nt', 'os', 'posix', 'register_archive_format', 'register_unpack_format', 
 'rmtree', 'stat', 'sys', 'unpack_archive', 'unregister_archive_format', 
 'unregister_unpack_format', 'warnings', 'which

'''

python_path = shutil.which("python")
print(python_path)


ls_path = shutil.which("ls")
print(ls_path)

# Creating a dummy file to demostrate copy
def create_file(file_name, dir):
    file_path = os.path.join(dir, file_name)

    os.makedirs(os.path.dirname(file_path), exist_ok=True) 

    # Create and write to the file
    with open(file_path, 'w') as file:
        file.write("This file was created to demonstrate use of shutil.copyfile.\n")
    
# Purpose: To copy a file from one directory, to another

def copy_file(src_dir, dest_dir, filename):
    source_path = os.path.join(src_dir, filename)
    dest_path = os.path.join(dest_dir, filename)

    print(source_path)
    print(dest_path)

    if os.path.exists(dest_path):
        print("file already exists. So, deleting")
        os.remove(dest_path)
    if not os.path.exists(dest_dir):
        print("creating dest_dir")
        os.makedirs(dest_dir)

    shutil.copyfile(source_path, dest_path)


create_file("test_file_1.txt", "test_dir_1")

copy_file("test_dir_1", "test_dir_2", "test_file_1.txt")