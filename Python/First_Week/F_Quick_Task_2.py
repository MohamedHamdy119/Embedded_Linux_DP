#!/usr/bin/python3

'''
python code that handle the following login system:

User Name  Password
Ahmed      1394
Ali        6078
Amr        9345

If the data entered is correct, the system shall show a welcome message, if not the system will print incorrect entry
'''

login_data = [
    ["Ahmed", "1394"],
    ["Ali", "6078"],
    ["Amr", "9345"]
]

username = input("User Name: ")
password = input("Password: ")

if [username, password] in login_data:
    print("Welcome!")
else:
    print("Incorrect Entry.")
