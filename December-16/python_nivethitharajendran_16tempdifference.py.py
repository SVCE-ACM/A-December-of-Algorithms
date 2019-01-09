import requests,json


api_key = "97db6bc1594ce5e535b3d93b22f2ee66"


base_url = "http://api.openweathermap.org/data/2.5/weather?"


city1=input("Enter city 1 name: ")
city2=input("Enter city 2 name:")

url1=base_url + "appid=" + api_key + "&q=" + city1
url2=base_url + "appid=" + api_key + "&q=" + city2

response1=requests.get(url1)
response2=requests.get(url2)

x1=response1.json()
x2=response2.json()

if x1["cod"] != "404":
	y1= x1["main"]
	temp1= y1["temp"]

else:
	print(" City Not Found ")

if x2["cod"] != "404":
	y2= x2["main"]
	temp2 = y2["temp"]
else:
	print(" City Not Found ")

print("The temperature difference is:",int(temp1-temp2),"degree celcius")
