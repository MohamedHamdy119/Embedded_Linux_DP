#!/usr/bin/python3

#python program to access environment variables.

import os

sel=int(input("Choose :\n1-ALL  environment variables\n2-PATH environment variable\n3-HOME environment variable\n-> "))

if sel == 1:
    print(f"All Environment Variables:{os.environ}")

elif sel == 2 :
    path = os.environ.get("PATH")
    print(f"PATH:{path}")

elif sel == 3 :
    home = os.environ.get("HOME")
    print(f"HOME:{home}")

else :
    print("Invalid Entry")
