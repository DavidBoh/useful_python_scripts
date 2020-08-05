#!/usr/bin/env python3
# Author David Boh // herrboh@live.com
import os


def create_hello():
    file_ext = ".c"
    filename = input("Please enter a name for your file: ")
    with open("{}{}".format(filename, file_ext), "w") as file:
        file.write("#include<stdio.h>\n")
        file.write("#include<stdlib.h>\n\n")
        file.write("int main(int argc, const char * argv[]){\n\n")
        file.write("\tprintf(\"Hello World!\\n\");\n\n")
        file.write("\treturn 0;\n")
        file.write("}\n")
    final_name = "{}{}".format(filename, file_ext)
    print("\nFile {} has been created\n".format(final_name))


create_hello()
