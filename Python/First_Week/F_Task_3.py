#!/usr/bin/python3

#Print the calendar of a given month and year

import calendar

year=int(input("Plese Enter The Year : "))
month=int(input("Plese Enter The Month : "))

if year > 0 and (month > 0 and month < 13) :
   print(calendar.month(year,month))
else :
   print("Invalid Entry") 