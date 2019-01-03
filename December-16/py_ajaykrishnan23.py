import configparser
import requests
import json
def getkey():
	config = configparser.ConfigParser()
	config.read("config.ini")
	return config["openweathermap"]["api"]
def getdata(apikey):
	data = []
	url = "http://api.openweathermap.org/data/2.5/weather?q=London,gb&mode=json&units=metric&appid="+str(apikey)
	data = requests.get(url)
	obj1  = data.json()
	#id1 = obj['id']
	url = "http://api.openweathermap.org/data/2.5/weather?q=Chennai,in&mode=json&units=metric&appid="+str(apikey)
	data = requests.get(url)
	obj2 = data.json()
	#id2 = obj['id']
	print('Temperature difference between '+str(obj2.get('name'))+ ' and ' + str(obj1.get('name'))+':'+str(obj2.get('main').get('temp')-obj1.get('main').get('temp')))
	
apikey = getkey()
getdata(apikey)










#response = requests.get("http://api.openweathermap.org/data/2.5/weather?id=" + str(id) +"&mode=json&units=metric&APPID="+APIKEY)
#print(response.content)