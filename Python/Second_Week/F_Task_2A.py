#!/usr/bin/python3

#Write a code to suggest automatically activates for you 

import webbrowser
import requests

url_act='https://www.boredapi.com/api/activity'

response_1=webbrowser.get('firefox')
response_1.open_new(url_act)

#Another Way

response_2 = requests.get(url_act) 
if response_2.status_code == 200:
    data = response_2.json()
    act = data["activity"]
    print(act)
    
else:
    print("Failed")