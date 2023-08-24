#!/usr/bin/python3

#Get your public IP

import webbrowser
import requests

url_ip = "https://api.ipify.org/?format=json"

response_1 = webbrowser.get('firefox')
response_1.open_new(url_ip)

#Another Way

response_2 = requests.get(url_ip) 
if response_2.status_code == 200:
    data = response_2.json()
    ip = data["ip"]
    print("YOR IP IS {}".format(ip))
    
else:
    print("Failed")