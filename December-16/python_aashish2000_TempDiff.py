import json
import requests
import datetime
import sys

api_key="Your Api Key"

base_url="http://api.openweathermap.org/data/2.5/weather?"

cities=list(map(str,input("Enter Cities:").split()))
complete_url1 = base_url + "appid=" + api_key + "&q=" + cities[0]
complete_url2 = base_url + "appid=" + api_key + "&q=" + cities[1]

resp1 = requests.get(complete_url1)
resp2 = requests.get(complete_url2)

x1 = resp1.json()
x2 = resp2.json()

if(x1["cod"]!="404" and x2["cod"]!="404"):

    y1=x1["main"]
    y2=x2["main"]

    curr_temp1=y1["temp"]
    curr_temp2=y2["temp"]

    diff=curr_temp1-curr_temp2
    now = datetime.datetime.now()
    print("Taken at ",end='')
    print(now.strftime("%H:%M (IST), %H:%M"))

    print("Current Temperature difference between",cities[0],"and",cities[1],"is",str(int(diff)),"°C")

else:
    print("Error")

    

