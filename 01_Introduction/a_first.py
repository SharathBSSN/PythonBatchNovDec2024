#!/usr/bin/python3

""" 
    Purpose: This ia a doc String
    Python Enhancement Proposal (PEP) - 8 Coding Style Guide (https://peps.python.org/pep-0008/)

    ###### - to remove a file via cmd -> rm <fileName>
             to rename a file via cmd -> mv <current_fileName> <new_fileName>
    
    To make a file executable

        to vew previlages
        
            ls -l
        
        assigin r(read)w(write)x(exe) previlages 
            
            chmod +x <fileName>

        to run the file
            
            ./<fileName>.extension

            -> to facilitate this, add the below at the top of the file

                #!/usr/bin/python3  --->>> SHEBANG LINE

                **@SharathBSSN ➜ /workspaces/PythonBatchNovDec2024/class01 (class01) $ which python -> /home/codespace/.python/current/bin/python

"""

def greetings(name):
    greet = "How are you da {2}?".format(name[0], name[1], name[2])
    print(greet)


greetings(["kotha", "Bunty", "Challa"])

