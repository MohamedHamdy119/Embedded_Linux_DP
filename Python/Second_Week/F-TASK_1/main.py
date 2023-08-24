#!/usr/bin/python3
import firelink

ip=int(input("Plese,Choose the website\n1- Facebook\n2- Linkedin\n3- Youtube\n4- Github\n5- Instagram\n"))

if ip in {1,2,3,4,5}:  
 firelink.Choose_Site(ip)
else:
 print("NOT VALED ENTER ....")
