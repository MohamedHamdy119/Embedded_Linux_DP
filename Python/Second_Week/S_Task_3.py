#!/usr/bin/python3
#Write a Python program to get the command-line arguments

import sys


print("This is the name/path of the script: {}".format(sys.argv[0]))
print("('Number of arguments:', {})".format(len(sys.argv)))
print('''('Argument List:', "{}")'''.format(str(sys.argv)))