#!/usr/bin/python3
#Python program to parse header file and read
#all prototypes of function and insert it into
#excel sheet with unique ID start with IDX0

import openpyxl

file = open("test.h")
data=file.read()
ls=data.split("\n")

work_book = openpyxl.Workbook()
sheet = work_book.active
for i in range(0,len(ls)):
 sheet["A{}".format(i+1)] = ls[i]
 sheet["B{}".format(i+1)] = "IDX{}".format(i)

work_book.save("test.xlsx")

