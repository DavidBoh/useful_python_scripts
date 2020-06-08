#!/usr/bin/env python3
#Author David Boh // herrboh@live.com
import os

def createpy():
    file_ext = ".py"
    filename = input("Please enter a name for your file: ")
    file = open("{}{}".format(filename,file_ext), "w")
    if file_ext == ".py":
        file.write("#!/usr/bin/env python3\n")
        final_name= "{}{}".format(filename,file_ext)
        os.chmod(final_name,0o755)
    print("\nFile {} has been created\n".format(final_name))
    file.close()
    creation()

def createbash():
    file_ext = ".sh"
    filename = input("Please enter a name for your file: ")
    file = open("{}{}".format(filename,file_ext), "w")
    if file_ext == ".sh":
        file.write("#!/bin/sh\n")
        final_name= "{}{}".format(filename,file_ext)
        os.chmod(final_name,0o755)
    print("\nFile {} has been created\n".format(final_name))
    file.close()
    creation()
    
def creation():
    """this script creates a .py or .sh file based on user input 
    Each file will be created with execute permissions and inside of each file, 
    the first line wille include its respective shebang #! line argument"""
    
    file_ext = ""
    active = True
    while active:
        bash_or_py = input("\nPlease choose file type\npress s for sh\npress p for pyhton\npress q to quit\n\n")
        
        if bash_or_py == 'q':
            active = False
            break
        
        if bash_or_py == 'p':
            createpy()          
            break

        if bash_or_py == 's':
            createbash()
            break

        if bash_or_py != 's' or bash_or_py != 'p' or bash_or_py != 'q':
            print("\nInvalid Input\n")
            creation()
            break

creation()
