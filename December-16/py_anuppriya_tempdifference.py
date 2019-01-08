import json
import requests
import datetime
now=datetime.datetime.now()
res1=requests.get("http://api.openweathermap.org/data/2.5/weather?id=1264527&units=metric&APPID=11111121111a")
data1=res1.json()
temp1=(data1["main"]["temp"])
res2=requests.get("http://api.openweathermap.org/data/2.5/weather?id=2643743&units=metric&APPID=11111121111a")
data2=res2.json()
temp2=(data2["main"]["temp"])
print("Taken at ",now.strftime("%H:%M"),"(IST),",now.strftime("%d-%m-%y"))
print("Current temperature difference between Chennai,TN and London,GB is ",temp1-temp2,"\u00b0C")

