#!/usr/bin/env python3

table_number = int(input("Please enter the number: "))

for i in range(1,11):
    print(("{} * " + str(table_number) + " = {}").format(i, i * table_number))
