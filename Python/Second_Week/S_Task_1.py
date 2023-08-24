#!/usr/bin/python3
import math

#Write python code to generate Init function of GPIO for AVR
def Init_PORTA_DIR():
    ip={}
    number=0
    for i in range(0,8):
        ip[i]=input("Please enter Bit {} mode: ".format(i))

    for i in range(0,8):
        if ip[i] =="in":
            number=number+0
        elif ip[i] =="out":
             number=int(number+math.pow(2,i))

    DDRA=bin(number)
    print(DDRA)

Init_PORTA_DIR()