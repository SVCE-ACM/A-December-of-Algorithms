import requests
import json
import datetime

apiKey ='1b5082a4a59a1c3a3a68ffaa6a1cb801'
url = 'http://api.openweathermap.org/data/2.5/weather?q='
country1='London, GB'
country2='Chennai'
resp1=requests.get(url+country1+'&APPID='+apiKey)
resp2=requests.get(url+country2+'&APPID='+apiKey)
temp1=0
temp2=0
if(resp1.ok):
    json1=json.loads(resp1.content)
    temp1=json1['main']['temp']
if(resp2.ok):
    json2=json.loads(resp2.content)
    temp2=json2['main']['temp']
#print(temp1)
#print(temp2)
temp=temp2-temp1
now=datetime.datetime.now()
print('Taken at '+str(now.hour)+':'+str(now.minute)+' (IST), '+str(now.day)+'-'+str(now.month)+'-'+str(now.year))
print('Current Temperature difference between Chennai,TN and London,GB is '+str(temp))
