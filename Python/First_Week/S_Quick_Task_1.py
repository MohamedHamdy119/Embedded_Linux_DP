#!/usr/bin/python3

#the largest item from a given list using loop

ls=input("Enter the list split by ',' : ").split(",")

for i in range(0,len(ls)) :
    ls[i]=int(ls[i])

print("The largest number in the list is {}".format(max(ls)))