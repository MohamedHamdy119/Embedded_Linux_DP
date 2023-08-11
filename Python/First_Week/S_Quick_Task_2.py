#!/usr/bin/python3

#code to find automatically bitcoin rate

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
    
if response.status_code == 200:
    data = response.json()
    rate = data["bpi"]["USD"]["rate"]
    print("Current Bitcoin rate: {} USD".format(rate))
else:
    print("Failed to retrieve Bitcoin rate.")