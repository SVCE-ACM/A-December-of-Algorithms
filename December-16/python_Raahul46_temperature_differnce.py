#!python3

"""
Hi there.
This file doesn't contain any code.
It's just here to give an example of the file naming scheme.
Cheers!
"""
import requests,json


api_key = "8af56c91890726fc507de74a7eee305b"


base_url = "http://api.openweathermap.org/data/2.5/weather?"


city_name = input("Enter city name : ")
city_name1=input("Enter city name 2:")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name
complete_url1= base_url + "appid=" + api_key + "&q=" + city_name1

response = requests.get(complete_url)
response1=requests.get(complete_url1)

x = response.json()
x1=response1.json()

if x["cod"] != "404":
	y = x["main"]
	current_temperature = y["temp"]
	print(" Temperature at ",city_name,"(in kelvin unit) = " +
					str(current_temperature) )


else:
	print(" City Not Found ")

if x1["cod"] != "404":
	y1 = x1["main"]
	current_temperature1 = y1["temp"]
	print(" Temperature at ", city_name1, "(in kelvin unit) = " +
		  str(current_temperature1))
else:
	print(" City Not Found ")

print("THE DIFFERENCE IN THE TEMPERATURE BETWEEN TWO CITIES IS:",current_temperature-current_temperature1)
