#!/usr/bin/python3

#Python program to test whether a passed letter is a vowel or not.

lett=input("Enter the Letter : ")
if (lett.lower()) in ['a','e','i','o','u'] :
    print("YES,the letter is vowel")
else :
   print("NO,the letter isn't vowel ")  