#!/usr/bin/python3

#Write a Python program to count the number of lines in a text file.
#write a Python program to count the Number of words in a file.

file=open("Python.txt")
data=file.read()
No_Of_Lines=len(data.split("\n"))
No_Of_Words=len(data.split())
file.close()
print("No of lines is {}\nNo of words is {}".format(No_Of_Lines,No_Of_Words))


#Write a Python program to write a “list” to a file.

Names  = ["Mohamed","Hamdy","Mohamed",21]
file=open("Python.txt","a")
file.write("\n")
for i in range(len(Names)):
    Names[i]=str(Names[i])
    file.write(" ".__add__(Names[i]))
file.close()