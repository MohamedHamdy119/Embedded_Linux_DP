#!/usr/bin/python3

#Get your location 

import webbrowser
import requests

url_ip = "https://api.ipify.org/?format=json"

response_1 = requests.get(url_ip) 
if response_1.status_code == 200:
    data = response_1.json()
    ip = data["ip"]

    response_2 = webbrowser.get('firefox')
    url_loc='https://ipinfo.io/{}/geo'.format(ip)
    response_2.open_new(url_loc)

else:
    print("Failed")