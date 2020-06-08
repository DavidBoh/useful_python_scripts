#!/usr/bin/env python3
#Author David Boh // herrboh@live.com
import os


def creation():
    """this script creates a .py or .sh file based on user input 
    Each file will be created with execute permissions and inside of each file, 
    the first line wille include its respective shebang #! line argument"""
    
    file_ext = ""
    bash_or_py = input("Please choose filetype\npress b for bash\npress p for pyhton\npress q to quit\n")
    active = True
    while active:
        
        if bash_or_py == 'b':
            file_ext = ".sh"
            filename = input("Please enter a name for your file ")
            file = open("{}{}".format(filename,file_ext), "w")
            if file_ext == ".sh":
                file.write("#!/bin/sh\n")
                final_name= "{}{}".format(filename,file_ext)
                os.chmod(final_name,0o755)
            print("File {} has been created".format(final_name))
            file.close()
            break
        elif bash_or_py == 'p':
            file_ext = ".py"
            filename = input("Please enter a name for your file ")
            file = open("{}{}".format(filename,file_ext), "w")
            if file_ext == ".py":
                file.write("#!/usr/bin/env python3\n")
                final_name= "{}{}".format(filename,file_ext)
                os.chmod(final_name,0o755)
            print("File {} has been created".format(final_name))
            file.close()
            break
        elif bash_or_py == 'q':
            active = False
        elif bash_or_py != 'b' or bash_or_py != 'p' or bash_or_py != 'q':
            print("\nInvalid Input\n")
            creation()
            
            
creation()
  



    

    

