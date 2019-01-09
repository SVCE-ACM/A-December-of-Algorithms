import requests,json
def getKey():
	with open('key.txt') as f:
		for line in f:
			return(line)
api_key = getKey()
url = "http://api.openweathermap.org/data/2.5/weather?appid="+api_key+"&q="
city1 = input('Enter name of first city: ')
city2 = input('Enter name of second city: ')
url1 = url+city1
url2 = url+city2
resp1 = requests.get(url1).json()
resp2 = requests.get(url2).json()
try:
	temp1 = resp1['main']['temp']
	temp2 = resp2['main']['temp']
	print('Current Temperature difference between '+city1+' and '+city2+' is '+str(temp1-temp2)+'°C')
except:
	print('Error! City not found')
